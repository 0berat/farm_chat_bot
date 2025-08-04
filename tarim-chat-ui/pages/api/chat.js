export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { question } = req.body;

  try {
    // Backend FastAPI'ye istek atıyoruz
    const response = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      throw new Error("Backend’den cevap alınamadı");
    }

    const data = await response.json();

    // Backend’den gelen cevabı frontend’e gönderiyoruz
    res.status(200).json({ answer: data.answer });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
