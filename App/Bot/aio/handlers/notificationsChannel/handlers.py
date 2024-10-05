import asyncio

from aiogram import F, types, Router

from Bot.aio.filters import AllowedChannels
from Bot.repository.matchSearch import getMatching
from Bot.properties import REQESTS_INTERVAL


router = Router()
router.channel_post.filter(AllowedChannels())


@router.channel_post(F.text)
async def text_handler(message: types.Message):
    text = message.text

    matchingIds = getMatching(text)
    
    for id in matchingIds:
        try:
            await message.bot.send_message(chat_id = id, text = text)
            await asyncio.sleep(REQESTS_INTERVAL)
        except Exception as e:
            print(f"Не удалось отправить сообщение пользователю {id}: {e}")


@router.channel_post(F.photo)
async def photo_handler(message: types.Message):

    if message.caption not in (None, ""):
        text = message.caption
        matchingIds = getMatching(text)
    
        for id in matchingIds:
            try:
                await message.bot.send_photo(chat_id = id, photo = message.photo[-1].file_id, caption = text)
                await asyncio.sleep(REQESTS_INTERVAL)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {id}: {e}")
        
    


@router.channel_post(F.video)
async def video_handler(message: types.Message):

    if message.caption not in (None, ""):
        text = message.caption
        matchingIds = getMatching(text)
    
        for id in matchingIds:
            try:
                await message.bot.send_video(chat_id = id, video = message.video.file_id, caption = text)
                await asyncio.sleep(REQESTS_INTERVAL)
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {id}: {e}")
    
        
