'use client'

import { useState } from 'react'

type Message = {
  role: 'user' | 'bot'
  text: string
}

export default function ChatPage() {
//   const [messages, setMessages] = useState<Message[]>([])
  const [messages, setMessages] = useState<Message[]>([
  { role: 'bot', text: 'Size nasıl yardımcı olabilirim? Ben Tarım Sohbet Asistanıyım, sorularınızı yanıtlamak için buradayım!' }
])

  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  const sendMessage = async () => {
    if (!input.trim()) return

    const userMessage: Message = { role: 'user', text: input }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const res = await fetch('http://localhost:8000/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: input }),
      })

      if (!res.ok) throw new Error(`Sunucudan hata döndü: ${res.status}`)

      const data = await res.json()
      const botMessage: Message = { role: 'bot', text: data.answer }
      setMessages(prev => [...prev, botMessage])
    } catch (error) {
      setMessages(prev => [...prev, { role: 'bot', text: 'Hata oluştu: ' + String(error) }])
    } finally {
      setLoading(false)
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && !loading) sendMessage()
  }

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-xl bg-white rounded-lg shadow-md p-4 flex flex-col">
        <div className="flex-1 overflow-y-auto space-y-4 mb-4 max-h-[500px]">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`text-sm p-3 rounded-lg w-fit max-w-[75%] ${
                msg.role === 'user'
                  ? 'bg-blue-500 text-white self-end ml-auto'
                  : 'bg-gray-200 text-gray-900 self-start'
              }`}
            >
            {msg.text.replace(/\*/g, '')}
            </div>
          ))}
          {loading && (
            <div className="text-gray-500 text-sm">Gemini düşünüyor...</div>
          )}
        </div>

        <div className="flex mt-auto">
          <input
            type="text"
            className="flex-1 border border-gray-300 rounded-l-lg p-2 focus:outline-none text-black placeholder-gray-500"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Mesajınızı yazın..."
            disabled={loading}
          />
          <button
            onClick={sendMessage}
            disabled={loading}
            className="bg-blue-600 text-white px-4 rounded-r-lg hover:bg-blue-700 disabled:opacity-50"
          >
            Gönder
          </button>
        </div>
      </div>
    </div>
  )
}
