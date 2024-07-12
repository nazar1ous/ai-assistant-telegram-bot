import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.setup import setup_routers

from config import credentials


async def main() -> None:
    bot = Bot(credentials["telegram_bot_token"],
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(setup_routers())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

