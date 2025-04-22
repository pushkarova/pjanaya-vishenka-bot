
import os
import random
import telebot
from telebot import types

# Токен бота, полученный от BotFather
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

questions = [
    "Самое странное, что ты делал/а в пьяном состоянии?",
    "Изменял ли ты своему партнеру? (Нынешнему или бывшему. Не важно)",
    "Что ты не мог/могла бы простить?",
    "Оставался ли ты когда- нибудь без копейки денег?",
    "У кого тебе легче одолжить деньги: у мужчины или у женщины?",
    "Какой ты видишь свою жизнь в ближайшие 5 лет?",
    "Есть ли человек, который ОЧЕНЬ хорошо к тебе относился и ты его до сих пор помнишь?",
    "Ты в личных отношениях (дружеских/любовных) пытаешься прояснить конфликтную ситуацию или 'пусть само течет и куда-то приведет'?",
    "Как ты справляешься с негативными эмоциями?",
    "Как ты принимаешь решения в сложных ситуациях?"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать в Пьяную Вишенку! Готовы сыграть?")
    bot.send_message(message.chat.id, "Для начала игры напишите /play")

@bot.message_handler(commands=['play'])
def play_game(message):
    question = random.choice(questions)
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    item = types.KeyboardButton("Ответить на вопрос")
    markup.add(item)
    bot.send_message(message.chat.id, f"Ваш вопрос: {question}", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def ask_question(message):
    bot.send_message(message.chat.id, "Если не хочешь отвечать — выпей рюмку!")
    
bot.polling()
