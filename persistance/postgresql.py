import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain_community.utilities.sql_database import SQLDatabase

load_dotenv()
POSTGRESQL_URI = os.getenv("POSTGRESQL_CONNECTION_STRING")

engine = create_engine(POSTGRESQL_URI)
sql_database = SQLDatabase(engine)
