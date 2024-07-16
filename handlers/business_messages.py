from aiogram import Router, F
from aiogram.types import Message
import time
import random
from generators.openai_utils import get_response_textual

router = Router()

ALLOWED_CONTENT_TYPES = [
    "text", "audio", "voice",
    "sticker", "document", "photo",
    "video"
]

@router.business_message(
    F.content_type.in_(
        ALLOWED_CONTENT_TYPES
    )
)
async def echo(message: Message) -> None:
    response = get_response_textual(str(message.chat.id), message.text)
    # sleep_time = random.randint(1, 30)
    # time.sleep(
    #     sleep_time
    # )

    await message.answer(response)