import google.generativeai as genai

genai.configure(api_key="api_key_gelicek")
# model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("domateste kullanilan ilaclar nedir  ")
# print(response.text)

# ✅ API KEY ile kimlik doğrulama (Bearer token değil)
# genai.configure(api_key="AIzaSyAjUkaRGElLGxBg5P8tWiOwRjHyFtKEaP0")

# Soru al
query = input("Soru: ")

# 🔎 Weaviate'den veri çekme
from haystack.document_stores import WeaviateDocumentStore
from haystack.nodes import EmbeddingRetriever

WEAVIATE_URL = "http://localhost"
INDEX_NAME = "TarimDocs"
model = genai.GenerativeModel("gemini-1.5-flash")  # veya "gemini-pro", "gemini-2.5-flash" vb.

document_store = WeaviateDocumentStore(WEAVIATE_URL, index=INDEX_NAME, embedding_dim=384)
retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    model_format="sentence_transformers"
)

# def ask_gemini(query: str) -> str:
#     # Weaviate'den ilgili dokümanları al
#     retrieved_docs = retriever.retrieve(query, top_k=3)
#     context = "\n\n".join([doc.content for doc in retrieved_docs])

#     # Prompt oluştur
#     prompt = f"Soru: {query}\n\nBilgi:\n{context}\n\nCevap:"

#     # Gemini modeline sor
#     response = model.generate_content(prompt)
#     return response.text

retrieved_docs = retriever.retrieve(query, top_k=3)
context = "\n\n".join([doc.content for doc in retrieved_docs])

prompt = f"Soru: {query}\n\nBilgi:\n{context}\n\nCevap:"

response = model.generate_content(prompt)

print("\n--- CEVAP ---")
print(response.text)
