from dotenv import load_dotenv
import os

load_dotenv()

from langchain_groq import ChatGroq
from utils.config import MODEL_NAME


if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")


llm = ChatGroq(
    model=MODEL_NAME,
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)

