import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

async function handleSubmit(e) {
  e.preventDefault();
  setLoading(true);
  setResponse("");

  try {
    const res = await fetch("http://localhost:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: query }),
    });

    if (!res.ok) {
      throw new Error("Sunucudan hata döndü: " + res.status);
    }

    const data = await res.json();
    setResponse(data.answer);
  } catch (error) {
    setResponse("Hata oluştu: " + error.message);
  } finally {
    setLoading(false);  // Bu satır kesin çalışacak
  }
}
  // Gelen yanıttaki ** karakterlerini " ile değiştir
  const formattedResponse = response.replace(/\*\*/g, '"');

  return (
    <div className="max-w-xl mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Akıllı Tarım Sohbet Asistanı</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Sorunuzu yazın..."
          className="w-full border border-gray-300 rounded p-2"
        />
        <button
          type="submit"
          disabled={loading}
          className="mt-2 bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          {loading ? "Yükleniyor..." : "Gönder"}
        </button>
      </form>

      <div className="whitespace-pre-wrap bg-gray-100 p-4 rounded min-h-[100px]">
        {formattedResponse}
      </div>
    </div>
  );
}
