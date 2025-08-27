from langgraph.checkpoint.memory import MemorySaver


def get_in_memory_checkpointer():
    """
    Creates and returns an in memory checkpointer

    Usage:
        graph = builder.compile(checkpointer=memory)
    """
    return MemorySaver()