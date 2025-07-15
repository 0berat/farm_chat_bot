import os
from haystack.document_stores import WeaviateDocumentStore
from haystack.nodes import EmbeddingRetriever
from haystack import Document
from haystack.utils import clean_wiki_text
from tqdm import tqdm

# Ayarlar
TXT_DIR = "/mnt/ikinci_disk/proje_tarim/tarim_proje_pdf/texts/"
# WEAVIATE_URL = "http://127.0.0.1:8031"

# 1. Weaviate'e bağlan
document_store = WeaviateDocumentStore(
    host="http://127.0.0.1", # Weaviate URL
    index="TarimDocs",
    embedding_dim=384,
    recreate_index=True  # her çalıştırmada temiz başlamak için
)

# 2. Retriever (Embedding için)
retriever = EmbeddingRetriever(
    document_store=document_store,
    embedding_model="sentence-transformers/all-MiniLM-L6-v2",  # Küçük ama etkili model
    model_format="sentence_transformers"
)

# 3. .txt dosyalarını al → parçalara böl → document oluştur
def load_documents(txt_folder):
    all_docs = []

    for fname in tqdm(os.listdir(txt_folder), desc="Dosyalar işleniyor"):
        if fname.endswith(".txt"):
            file_path = os.path.join(txt_folder, fname)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Chunk'lama (her 100 kelimede bir)
            chunks = [content[i:i+800] for i in range(0, len(content), 800)]
            for chunk in chunks:
                all_docs.append(Document(content=chunk, meta={"source": fname}))
    
    return all_docs

# 4. Belgeleri yükle
documents = load_documents(TXT_DIR)

# 5. Embedding hesapla
document_store.write_documents(documents)
document_store.update_embeddings(retriever)

print(f"✅ {len(documents)} belge başarıyla Weaviate'e yüklendi.")
