import google.generativeai as genai

genai.configure(api_key="api_key_gelicek")
from haystack.document_stores import WeaviateDocumentStore
from haystack.nodes import EmbeddingRetriever

WEAVIATE_URL = "http://localhost"
INDEX_NAME = "TarimDocs"
model = genai.GenerativeModel("gemini-1.5-flash") 

document_store = WeaviateDocumentStore(WEAVIATE_URL, index=INDEX_NAME, embedding_dim=384)
retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    model_format="sentence_transformers"
)

def ask_gemini(query: str) -> str:
    retrieved_docs = retriever.retrieve(query, top_k=3)
    context = "\n\n".join([doc.content for doc in retrieved_docs])

    prompt = f"Soru: {query}\n\nBilgi:\n{context}\n\nCevap:"

    response = model.generate_content(prompt)
    return response.text

