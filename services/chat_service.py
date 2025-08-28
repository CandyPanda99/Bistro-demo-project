from typing import AsyncGenerator

from langchain_core.messages import AIMessage
from langgraph.constants import START
from langgraph.graph import StateGraph
from langgraph.prebuilt import tools_condition

from agents.bistro_agent import bistro_assistant_runnable
from memory.mongodb_checkpointer import get_mongodb_checkpointer
from schemas.chat_request import ChatRequest
from tools.ddg_search_tool import ddg_search
from tools.information_tool import lookup_information
from tools.menu_agent_tool import menu_agent_tool
from tools.reservation_tool import reservation_tool
from tools.complaint_tool import complaint_tool
from utils.Assistant import Assistant

from utils.State import State
from utils.utils import create_tool_node_with_fallback


class ChatService:
    def __init__(self):
        self.tools = [
            ddg_search,
            lookup_information,
            menu_agent_tool,
            reservation_tool,
            complaint_tool
        ]
        self.assistant_runnable = bistro_assistant_runnable
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

        final_response = final_state['messages'][-1] if final_state['messages'] else None

        if isinstance(final_response, AIMessage):
            return final_response.content
        else:
            return "An error occurred, and no final response was generated."

    async def generate_streaming_response(self, request: ChatRequest) -> AsyncGenerator[str, None]:
        config = {
            "configurable": {
                "thread_id": request.session_id,
            }
        }

        async for event in self.agent_graph.astream_events(
            {"messages": ("user", request.query)},
            config=config,
            version="v1"
        ):
            kind = event["event"]
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    yield content
