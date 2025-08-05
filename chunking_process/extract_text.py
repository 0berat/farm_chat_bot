import os
import fitz  # PyMuPDF
import re

pdf_dir = "/mnt/ikinci_disk/proje_tarim/tarim_proje_pdf"
output_dir = "/mnt/ikinci_disk/proje_tarim/tarim_proje_pdf/texts/"

os.makedirs(output_dir, exist_ok=True)

def filtrele_gereksiz_satirlar(metin):
    satirlar = metin.split("\n")
    temiz = []
    for satir in satirlar:
        if any([
            "Tarım ve Orman Bakanlığı" in satir,
            "T.C." in satir and "İl Müdürlüğü" in satir,
            "Sayfa" in satir,  #kendini tekrar eden stringleri yoksayiyoruz.
            "www." in satir,
            satir.strip() == ""
        ]):
            continue
        temiz.append(satir)
    return "\n".join(temiz)

def temizle_metin(metin):
    return metin.strip()

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, filename)
        txt_path = os.path.join(output_dir, filename.replace(".pdf", ".txt"))

        try:
            with fitz.open(pdf_path) as doc:
                text = ""
                for page in doc:
                    raw = page.get_text()
                    filtred = filtrele_gereksiz_satirlar(raw)
                    cleaned = temizle_metin(filtred)
                    text += cleaned + "\n"

            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"[+] {filename} → {txt_path}")
        except Exception as e:
            print(f"[!] Hata: {filename} → {e}")
