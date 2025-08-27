from fastapi import FastAPI
from starlette.responses import JSONResponse

from routers import documents

app = FastAPI(
    title="Bistro AI Assistant",
    description="Bistro is an AI assistant that helps with restaurant operations, including menu management, customer service, and more.",
    version="1.0.1"
)

app.include_router(documents.router, prefix="/documents")

@app.get(path="/health", tags=["health"])
async def root():
    return JSONResponse(content={"message": "Service healthy"},status_code=200)
