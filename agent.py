import os
import sqlite3
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenAI
from langchain_core.messages import SystemMessage 
from langgraph.graph import StateGraph, START, END, MessageState 
from langgraph.prebuilt import ToolNose, tools_condition
from langgraph.checkpoint.sqlite import SqliteServer

Path("data").mkdir(exist_ok=True)

# Update default and allowed models to use Gemini 2.5
DEFAULT_MODELS = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

ALLOWED_MODEL = {
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gemini-2.5-flash-lite",
    "gemini-1.5-flash"
    "gemini-1.5-pro"
    
}



