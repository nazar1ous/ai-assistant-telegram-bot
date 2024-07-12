from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer("Hello! I'm a bot!")

@router.message(Command("help"))
async def help_command(message: Message, command: CommandObject):
    print(command.args)
    await message.answer("This is a help message!")