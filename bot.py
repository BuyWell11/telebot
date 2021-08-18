import logging
import asyncio
import config
import datetime
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

day_of_week = ['https://tenor.com/view/good-morning-monday-omg-gif-13889579', 'https://media1.tenor.com/images/2f772d813f7db3618432ea00c75bf64b/tenor.gif', 'https://memepedia.ru/wp-content/uploads/2018/07/cover1-768x512.jpg', 'https://www.meme-arsenal.com/memes/5a99fdfbb390d310e78afcd174e72d40.jpg', 'https://i.pinimg.com/originals/c0/20/61/c020615b843acf7e9c5f8d7ad1b2c984.gif', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAwGLaVdU_cXMw43WrVHYSYGcHP4Cq-mWAgA&usqp=CAU', 'https://img1.liveinternet.ru/images/attach/c/9/106/333/106333915_4746136_7_voskresene.jpg']

date = datetime.datetime.now()
date_string = date.strftime('%w')
print(date_string)


bot = Bot(token=config.token)
disp = Dispatcher(bot=bot)

def get_text_excluding_children(driver, element): 
	 return driver.execute_script(""" var parent = arguments[0]; var child = parent.firstChild; var ret = ""; while(child) { if (child.nodeType === Node.TEXT_NODE) ret += child.textContent; child = child.nextSibling; } return ret; """, element) 


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
    try:
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        @disp.message_handler(Text(equals="Какой сегодня день?"))
        async def with_puree(message: types.Video):
            await message.reply(day_of_week[int(date_string)-1])
            print(message)


        @disp.message_handler(commands="парфирич")
        async def parf(message: types.Message):
        	user_id=message.chat.id
        	

        @disp.message_handler()
        async def parfir(message: types.Message):
        	text = ""
        	user_id=message.chat.id
        	driver = webdriver.Chrome()
        	driver.get("https://porfirevich.ru")
        	element = driver.find_element_by_class_name("ql-editor")
        	element.send_keys(message.text)
        	element.send_keys(Keys.TAB)
        	await asyncio.sleep(10)
        	new_text = driver.find_elements_by_tag_name("strong")
        	for elem in range(len(new_text)):
        		if elem == 1:
        			text = get_text_excluding_children(driver, new_text[elem])
        			print(text)
        			break
        	await bot.send_message(chat_id=user_id,text=text)
        	driver.quit()
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())