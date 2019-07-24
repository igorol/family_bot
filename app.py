import os
import logging
import requests
from weather import get_weather, get_radar
from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    filename="log.txt",
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

token = os.environ["telegram_bot_token"]


def dog(bot, update):
    contents = requests.get("https://random.dog/woof.json").json()
    url = contents["url"]
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def jolie(bot, update):
    chat_id = update.message.chat_id
    with open("./media/jolie.webp", "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def weather(bot, update):
    chat_id = update.message.chat_id
    summary, tmax, tmin = get_weather()
    message = f"""Weather Summary for today: {summary},
    Max: {tmax},
    Min: {tmin}
    """
    bot.send_message(chat_id=chat_id, text=message)


def radar(bot, update):
    chat_id = update.message.chat_id
    fn = get_radar()
    with open(fn, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def main():
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("dog", dog))
    dp.add_handler(CommandHandler("jolie", jolie))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("buien", radar))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
