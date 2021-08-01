import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1945897379:AAHZCdGHYiqLKB2UAvB2GHMSnLPX0mBhzx8') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['documento'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    document = open('pagina33.docx', 'rb')
    bot.send_document(id, document)
@bot.message_handler(commands=['ubicacion'])
def ubicacion(mensaje):
    bot.send_chat_action(id, 'find_location')
    bot.send_location(id, 15.180827805165354, -87.88264510329708)
bot.polling()