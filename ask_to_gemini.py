import google.generativeai as genai

genai.configure(api_key="AIzaSyAjUkaRGElLGxBg5P8tWiOwRjHyFtKEaP0")
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

document_store = WeaviateDocumentStore(WEAVIATE_URL, index=INDEX_NAME, embedding_dim=384)
retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",
    model_format="sentence_transformers"
)

retrieved_docs = retriever.retrieve(query, top_k=3)
context = "\n\n".join([doc.content for doc in retrieved_docs])

# 🧠 Gemini'ye gönderilecek prompt
prompt = f"Soru: {query}\n\nBilgi:\n{context}\n\nCevap:"

# 🚀 Gemini'ye istek
model = genai.GenerativeModel("gemini-1.5-flash")  # veya "gemini-pro", "gemini-2.5-flash" vb.
response = model.generate_content(prompt)

# ✅ Yanıtı yazdır
print("\n--- CEVAP ---")
print(response.text)
