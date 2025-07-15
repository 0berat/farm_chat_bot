from google import genai

client = genai.Client(api_key="AIzaSyAjUkaRGElLGxBg5P8tWiOwRjHyFtKEaP0")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="selam dostum"
)
print(response.text)
