import asyncio

from aiogram import F, types, Router

from Bot import constants

router  = Router()

@router.message()
async def hello_responce(message:types.Message):
    await message.answer(constants.HELLO)
    await message.delete()