import telebot
import config
import datetime
from telebot import types

command = []

day_of_week = ['https://tenor.com/view/good-morning-monday-omg-gif-13889579', 'https://media1.tenor.com/images/2f772d813f7db3618432ea00c75bf64b/tenor.gif', 'https://memepedia.ru/wp-content/uploads/2018/07/cover1-768x512.jpg', 'https://www.meme-arsenal.com/memes/5a99fdfbb390d310e78afcd174e72d40.jpg', 'https://i.pinimg.com/originals/c0/20/61/c020615b843acf7e9c5f8d7ad1b2c984.gif', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAwGLaVdU_cXMw43WrVHYSYGcHP4Cq-mWAgA&usqp=CAU', 'https://img1.liveinternet.ru/images/attach/c/9/106/333/106333915_4746136_7_voskresene.jpg']

bot = telebot.TeleBot(config.token, parse_mode=None)

print('bot is working')

date = datetime.datetime.now()
date_string = date.strftime('%w')


def generate_inline_keyboard (*answer):
    keyboard = types.InlineKeyboardMarkup()
    temp_buttons = []
    for i in answer:
        temp_buttons.append(types.InlineKeyboardButton(text=i[0], callback_data=i[1]))
    keyboard.add(*temp_buttons)
    return keyboard


keyboard = generate_inline_keyboard(['Какой сегодня день?', 'day'])

print(date.strftime('%w %H'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	person_id = message.from_user.id
	bot.send_message(person_id,'П-п-п привет')


@bot.message_handler(content_types=['text', 'document', 'video'])
def greeting(message):
	if message.text.lower() == 'ку':
		bot.send_message(message.from_user.id, "Ку")
	elif message.text == 'Какой сегодня день?':
		bot.send_video(message.from_user.id,day_of_week[int(date_string)-1])



bot.polling(none_stop=True, interval=0)