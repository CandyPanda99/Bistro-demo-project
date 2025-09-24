import langchain
from fastapi import FastAPI
from starlette.responses import JSONResponse

from routers import document_router, chat_router

langchain.debug = True

app = FastAPI(
    title="Bistro AI Assistant",
    description="Bistro is an AI assistant that helps with restaurant operations, including menu management, customer service, and more.",
    version="1.0.1"
)

app.include_router(document_router.router, prefix="/documents")
app.include_router(chat_router.router, prefix="/agent")

@app.get(path="/health", tags=["health"])
async def root():
    return JSONResponse(content={"message": "Service healthy"},status_code=200)
