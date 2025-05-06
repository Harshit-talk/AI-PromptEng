import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print("Loaded API Key:", api_key[:10], "...")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("Give me a healthy recipe with broccoli and tofu.")
print(response.text)