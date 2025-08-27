from langchain_core.runnables import Runnable, RunnableConfig
from utils.State import State


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):
        while True:
            configuration = config.get("configurable", {})
            session_id = configuration.get("session_id", None)
            state = {**state, "user_info": session_id}
            result = self.runnable.invoke(state,verbose=True)
            if not result.tool_calls and (
                not result.content
                or isinstance(result.content, list)
                and not result.content[0].get("text")
            ):
                messages = state["messages"] + [("user", "Respond with a real output.")]
                state = {**state, "messages": messages}
            else:
                break
        return {"messages": result}