import os
import asyncio

from django.apps import AppConfig
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand

from Bot import constants

from Bot.aio.handlers.notificationsChannel.handlers import router as note_channels_router
from Bot.aio.handlers.users.handlers import router as users_private_router





bot = Bot(token = os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(note_channels_router)
dp.include_router(users_private_router)


async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates = True)
    await bot.set_my_description(constants.DESCRIPTION)
    await bot.set_my_commands(commands = constants.USER_COMMANDS,scope = types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)

async def stopBot() -> None:
    await dp.stop_polling()



async def on_startup(bot):
    print("Bot was started.")

async def on_shutdown(bot):
    print("Bot was down.")