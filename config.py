import os
from dotenv import load_dotenv


load_dotenv()
credentials = {
    "openai_api_key": os.getenv('OPENAI_API_KEY', "None"),
    "telegram_bot_token": os.getenv('TELEGRAM_BOT_TOKEN', "None")
}

settings = {
    "chatgpt_model": "gpt-4o",
    "gpt_4_model_max_tokens": 4096,
    "chatgpt_temperature": 0.7,
    "openai_timeout": 5000,
    "max_retries": 2,
    "seed": 42,
}
