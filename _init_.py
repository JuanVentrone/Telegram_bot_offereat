import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Veamos que es lo que sucede"""
    update.message.reply_text('Hola, esto es una prueba, ornella')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('ayuuuuuda')


def nella(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Toca las tetas de nella')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1203014270:AAEcmANbEwlLCtDqCW_xogdgUMU92xh9cxc", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("nella", nella))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


# from telegram.ext import Updater
# updater = Updater(token='1203014270:AAEcmANbEwlLCtDqCW_xogdgUMU92xh9cxc', use_context=True)

# dispatcher = updater.dispatcher

# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                      level=logging.INFO)

# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Nella Mamamelo")

# from telegram.ext import CommandHandler
# start_handler = CommandHandler('start', start)
# dispatcher.add_handler(start_handler)

# updater.start_polling()

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="No entiendo ni verga")

# update

# from telegram.ext import MessageHandler, Filters
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)