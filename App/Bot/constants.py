from aiogram.types import BotCommand

GITHUB = "https://github.com/Chazarov/Alerts-tg-bot"

ADMIN_LINK = "https://t.me/ZAM_Andrew"

DESCRIPTION = "/help - подробности"

HELLO = f"🤖: Привет✋ Этот бот создан для сортировки оповещений. \n" +\
    f"Его исходники есть на моем Github:\n" +\
    f"{GITHUB}\n" +\
    f"По остальным вопросам можете обращатся к разработчику: {ADMIN_LINK}🧑🏻‍💻"



USER_COMMANDS = [
    BotCommand(command='help', description='Помощь'),
]