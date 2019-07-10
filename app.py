from telegram.ext import Updater, CommandHandler, RegexHandler
import requests
import re
import logging

logging.basicConfig(level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

token = '828032240:AAHllyNsu_SsrLSq4QjkmaGbs3iZw3sS2vM'

def dog(bot, update):
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def jolie(bot, update):
    chat_id = update.message.chat_id
    with open('./media/jolie.webp', 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog', dog))
    dp.add_handler(CommandHandler('jolie', jolie))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
