import logging
import asyncio
import config
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

day_of_week = ['https://tenor.com/view/good-morning-monday-omg-gif-13889579', 'https://media1.tenor.com/images/2f772d813f7db3618432ea00c75bf64b/tenor.gif', 'https://memepedia.ru/wp-content/uploads/2018/07/cover1-768x512.jpg', 'https://www.meme-arsenal.com/memes/5a99fdfbb390d310e78afcd174e72d40.jpg', 'https://i.pinimg.com/originals/c0/20/61/c020615b843acf7e9c5f8d7ad1b2c984.gif', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAwGLaVdU_cXMw43WrVHYSYGcHP4Cq-mWAgA&usqp=CAU', 'https://img1.liveinternet.ru/images/attach/c/9/106/333/106333915_4746136_7_voskresene.jpg']

date = datetime.datetime.now()
date_string = date.strftime('%w')
print(date_string)


async def start_handler(event: types.Message):
    await event.answer(
        f"Ку, {event.from_user.get_mention(as_html=True)}",
        parse_mode=types.ParseMode.HTML,
    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Какой сегодня день?"]
    keyboard.add(*buttons)
    await event.answer("Ну что делать будем?", reply_markup=keyboard)


async def main():
    bot = Bot(token=config.token)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        @disp.message_handler(Text(equals="Какой сегодня день?"))
        async def with_puree(message: types.Video):
            await message.reply(day_of_week[int(date_string)-1])
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())