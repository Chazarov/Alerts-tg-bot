import asyncio

from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError





class Command(BaseCommand):
    help = "Launching the bot"

    def handle(self, *args, **options):
        try:
            from dotenv import find_dotenv, load_dotenv
            load_dotenv(find_dotenv())
            from Bot.main import main

            asyncio.run(main())

        except ValidationError as e:
            print("Error: Unable to start bot")



        self.stdout.write(self.style.SUCCESS('Bot was started'))