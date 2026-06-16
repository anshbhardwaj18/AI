from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os

app = FastAPI()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)
class ChatRequest(BaseModel):
    prompt: str
@app.post("/chat")
def chat(data: ChatRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=data.prompt
    )

    return {"response":response.text}

