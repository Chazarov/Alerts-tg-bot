from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from Bot.models import Channels

class AllowedChannels(Filter):

    ids:str

    
    def __init__(self) -> None:
        print("INIT FILTER: ", end="")
        objs = Channels.objects.all()
        self.ids = [x.channel_id for x in objs]
        print(self.ids)

        return

    async def __call__(self, message:Message) -> bool:
        print("Filter Use: ", end="")
        if len(self.ids) == 0:
            print("False")
            return False
        if str(message.chat.id) in str(self.ids):
            print("True")
            return True