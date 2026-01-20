from google import genai
from keys import API_KEY

print("Starting...")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="models/gemini-2.5-flash",
    contents="Answer in short: Give 3 business domains where AI won't ever be used."
)

print(response.text)
