from dotenv import load_dotenv
import os

print("Config.py is Loading...")
load_dotenv()

LOG_LEVEL=os.getenv("LOG_LEVEL", "INFO")
APP_NAME=os.getenv("APP_NAME","Text Utility API")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "deepseek/deepseek-chat-v3-0324:free"
)