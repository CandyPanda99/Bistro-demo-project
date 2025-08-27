import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from persistance.pinecone_db import get_pinecone_vector_db, index

router = APIRouter()

@router.post("/upload", tags=["documents"])
async def upload_document(file: UploadFile = File(...)):
    """
    Uploads a markdown file, processes it, and adds it to the vector store.
    """
    temp_file_path = f"data/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())

    loader = UnstructuredMarkdownLoader(temp_file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    vector_db = get_pinecone_vector_db()
    vector_db.add_documents(splits)

    os.remove(temp_file_path)

    return {"message": "Document uploaded and processed successfully."}

@router.delete("/", tags=["documents"])
async def delete_all_documents():
    """
    Deletes all documents from the vector store.
    """
    index.delete(delete_all=True)
    return {"message": "All documents deleted successfully."}

@router.delete("/{document_id}", tags=["documents"])
async def delete_document(document_id: str):
    """
    Deletes a specific document by its ID.
    """
    try:
        index.delete(ids=[document_id])
        return {"message": f"Document {document_id} deleted successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get(
    path="/search/",
    tags=["documents"],
    description="Search for a query in the Pinecone index",
)
def search(query: str, limit: int = 10):
    """
    Search for a query in the Pinecone index
    - **query**: The query to search for
    """
    vector_store = get_pinecone_vector_db()
    results = vector_store.similarity_search(query=query,k=limit)
    print(results)
    return results