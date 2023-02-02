import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
    response = req.json()
    sell_price = response['btc_usd']['sell']
    print(f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price :{sell_price}')

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, f"Hello,{message.from_user.first_name}!\n"
                                          f"Write the 'price' to check the cost of BTC")

    @bot.message_handler(content_types=['text'])
    def show_price(message):
        if message.text.lower() == 'price':
            try:
                req = requests.get('https://yobit.net/api/3/ticker/btc_usd')
                response = req.json()
                sell_price = response['btc_usd']['sell']
                bot.send_message(message.chat.id,
                                 f'{datetime.now().strftime("%Y-%m-%d %H:%M")}\nSell BTC price :{sell_price}')
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id,
                                 "Damn...Something was wrong")
        else:
            bot.send_message(message.chat.id,
                             "Sorry, i only understand command 'price' !")

    bot.polling()

if __name__ == '__main__':
    telegram_bot(token)
    