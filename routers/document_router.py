import re

from fastapi import APIRouter, UploadFile, File, HTTPException
from langchain_core.documents import Document
from persistance.pinecone_db import get_pinecone_vector_db, index

router = APIRouter()

@router.post("/upload", tags=["documents"])
async def upload_document(file: UploadFile = File(...)):
    """
    Uploads a markdown file, processes it by splitting on H2 headings,
    and adds the chunks to the vector store.
    """
    try:
        contents = await file.read()
        faq_text = contents.decode('utf-8')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {e}")

    split_pattern = r"(?=\n##\s)"
    chunks = [chunk.strip() for chunk in re.split(split_pattern, faq_text) if chunk.strip()]
    documents_to_add = [Document(page_content=txt) for txt in chunks]

    if not documents_to_add:
        raise HTTPException(status_code=400, detail="No content found in the document after splitting.")

    vector_db = get_pinecone_vector_db()
    vector_db.add_documents(documents_to_add)

    return {"message": f"Document uploaded and processed successfully into {len(documents_to_add)} chunks."}

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