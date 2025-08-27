import uuid
from datetime import datetime

from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.constants import START
from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition

from constants.prompts import BISTRO_AGENT_SYSTEM_PROMPT
from memory.mongodb_checkpointer import get_mongodb_checkpointer
from models.chat_models.chat_openai import get_openai_chat
from schemas.chat_request import ChatRequest
from tools.ddg_search_tool import ddg_search
from tools.information_tool import lookup_information
from tools.menu_agent_tool import menu_agent_tool

from utils.State import State
from utils.utils import create_tool_node_with_fallback


class ChatService:
    def __init__(self):
        self.tools = [
            ddg_search,
            lookup_information,
            menu_agent_tool
        ]
        self.llm = get_openai_chat()
        self.primary_assistant_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    BISTRO_AGENT_SYSTEM_PROMPT,
                ),
                ("placeholder", "{messages}"),
            ]
        ).partial(time=datetime.now)
        self.assistant_runnable = self.primary_assistant_prompt | self.llm.bind_tools(self.tools)
        self.agent_graph = self._build_graph()

    def _build_graph(self):
        builder = StateGraph(State)
        builder.add_node("assistant", Assistant(self.assistant_runnable))
        builder.add_node("tools", create_tool_node_with_fallback(self.tools))
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges(
            "assistant",
            tools_condition,
        )
        builder.add_edge("tools", "assistant")
        memory = get_mongodb_checkpointer()
        return builder.compile(checkpointer=memory)

    def generate_response(self, request: ChatRequest) -> str:
        config = {
            "configurable": {
                "thread_id": request.session_id,
            }
        }

        final_state = self.agent_graph.invoke(
            {"messages": ("user", request.query)},
            config=config,
        )

        print("\n\n-- VERBOSE EXECUTION LOG --\n")
        if final_state and "messages" in final_state:
            for message in final_state["messages"]:
                print(message.pretty_repr())
        print("\n-- END OF LOG --\n\n")

        final_response = final_state['messages'][-1] if final_state['messages'] else None

        if isinstance(final_response, AIMessage):
            return final_response.content
        else:
            return "An error occurred, and no final response was generated."
