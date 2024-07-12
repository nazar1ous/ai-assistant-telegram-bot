from aiogram import Router, F
from aiogram.types import Message

from generators.setup import gpt_model, memory
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
    response = get_response_textual(gpt_model, memory, message.text)

    await message.answer(response)