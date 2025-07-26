import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use a valid model name from the list
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def generate_questions(tech_stack):
    prompt = f"""
You are a technical interviewer.
Generate 3 to 5 technical interview questions for a candidate
who has experience in: {tech_stack}.
Make questions relevant to each technology mentioned.
Only include the questions, not the answers.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating questions: {str(e)}"
