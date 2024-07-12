from langchain.chat_models import ChatOpenAI
from langchain.memory.buffer import ConversationBufferMemory
from config import credentials, settings
memory = ConversationBufferMemory(return_messages=True)

gpt_model = ChatOpenAI(
    openai_api_key=credentials["openai_api_key"],
    max_retries=settings["max_retries"],
    temperature=settings["chatgpt_temperature"],
    model=settings["chatgpt_model"],
    max_tokens=settings["gpt_4_model_max_tokens"],
    n=1,
    timeout=settings["openai_timeout"],
    seed=settings["seed"]
)
