from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

# Pdf ler icersinden aldigim referans cümle ve model den aldigim cevap karsilastirmasi ile blue skorum 0.11 cikmaktadir.

reference = [['Beklenmeyen', 'bir', 'etki', 'gözlemlendiğinde', 'bu', 'durum', 'ayrıntılı', 'şekilde', 'kayıt', 'altına', 'alınmalı', 've', 'rapor', 'edilmelidir.']]

candidate = ['Deneme', 'sırasında', 'beklenmeyen', 'bir', 'etki', 'gözlemlenirse', 'tüm', 'gözlemler', 'detaylı', 'olarak', 'kaydedilmeli', 've', 'rapor', 'edilmelidir.']

smoothie = SmoothingFunction().method4

score = sentence_bleu(reference, candidate, smoothing_function=smoothie)

print(f"BLEU skoru: {score:.2f}")