import os

import certifi
from dotenv import load_dotenv
from pymongo import MongoClient, AsyncMongoClient
from langgraph.checkpoint.mongodb import MongoDBSaver, AsyncMongoDBSaver

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_CONNECTION_STRING")

def get_mongodb_checkpointer():
    """
    Creates and returns a MongoDBSaver checkpointer.

    Usage:
        checkpointer = MongoDBSaver(mongodb_client)
        graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    """
    return MongoDBSaver(MongoClient(MONGODB_URI,tlsCAFile=certifi.where()))

def get_mongodb_async_checkpointer():
    """
    Creates and returns a MongoDBSaver checkpointer.

    Usage:
        checkpointer = AsyncMongoDBSaver(async_mongodb_client)
        graph = create_react_agent(model, tools=tools, checkpointer=checkpointer)
    """
    return AsyncMongoDBSaver(AsyncMongoClient(MONGODB_URI,tlsCAFile=certifi.where()))