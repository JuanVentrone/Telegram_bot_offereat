import logging
import pandas as pd
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




update = telegram.ext.Updater('1203014270:AAEcmANbEwlLCtDqCW_xogdgUMU92xh9cxc')
bot = update.bot
dp = update.dispatcher



HELP_BUTTON_CALLBACK_DATA = 'A unique text for help button callback data'
help_button = telegram.InlineKeyboardButton(
    text='Help me', # text that show to user
    callback_data=HELP_BUTTON_CALLBACK_DATA # text that send to bot when user tap button
    )


def start(bot, update):
    # try:
    #     chat_id = bot.get_updates()[-1].message.chat_id
    # except IndexError:
    chat_id = 0
    bot.send_message(
        chat_id=chat_id,
        text='Hello ...',
        reply_markup=telegram.InlineKeyboardMarkup([help_button]),
        )

def command_handler_help(bot, update):
    chat_id = update.message.from_user.id
    bot.send_message(
        chat_id=chat_id,
        text='Help text for user ...',
        )
def callback_query_handler(bot, update):
    cqd = update.callback_query.data
    #message_id = update.callback_query.message.message_id
    #update_id = update.update_id
    if cqd == HELP_BUTTON_CALLBACK_DATA:
        command_handler_help(bot, update)
    # elif cqd == ... ### for other buttons

print('Your bot is --->', bot.username)
dp.add_handler(telegram.ext.CommandHandler('start', start))
dp.add_handler(telegram.ext.CommandHandler('help', command_handler_help))
dp.add_handler(telegram.ext.CallbackQueryHandler(callback_query_handler))
update.start_polling()