import os

from django.apps import AppConfig
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand

from Bot import properties



bot = Bot(token = os.getenv("TOKEN"))
dp = Dispatcher()

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bot'

    def ready(self):
        


        print(" --Bot started-- ")


async def main()->None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await bot.delete_webhook(drop_pending_updates = True)
    await bot.set_my_description(properties.description)
    await bot.set_my_commands(commands = properties.user_commands,scope = types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


async def on_startup(bot):
    print("Bot was started.")

async def on_shutdown(bot):
    print("Bot was down.")