from aiogram import Router
from aiogram.filters import Filter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from Bot.models import Channels

class AllowedChannels(Filter):

    ids:str

    def __init__(self) -> None:
        objs = Channels.objects.all()
        self.ids = [x.id for x in objs]

        return

    async def __call__(self, message:Message) -> bool:
        if len(self.ids) == 0:
            return False
        if message.chat.id in self.ids:
            return True