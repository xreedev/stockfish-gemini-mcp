import google.generativeai as genai
from .prompts import system_prompt
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_evaluation(summary : str) -> str :
    prompt = system_prompt.SYSTEM_PROMPT
    return model.generate_content(prompt + summary).text