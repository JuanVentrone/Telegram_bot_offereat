import logging
import pandas as pd
import telegram
import numpy as np
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler


# Reading Data
data = pd.read_csv("ig_scrapper/database/uni data/data_v1.01.csv")
# selection food
class fd:

    postre =     ('clasificacion', 'postre')
    desayuno =   ('clasificacion', 'desayuno')
    gourmet =    ('clasificacion', 'gourmet')
    chatarra =   ('clasificacion', 'chatarra')
    combo =      ('combo', True)
    pasapalos =  ('clasificacion', 'pasapalo')
    cumple =     ('Tortas',True)





# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

token = "1203014270:AAEcmANbEwlLCtDqCW_xogdgUMU92xh9cxc"
bot = telegram.Bot(token=token)

try:
    chat_id = bot.get_updates()[-1].message.chat_id
except IndexError:
    chat_id = 0

    
# def prueba(update, context):
        
        
        
#         update.callback_query.message.reply_text('Message of the day')
#         context.bot.send_photo(chat_id=update.effective_chat.id, photo = open( 'ig_scrapper/database/images/image0.jpg','rb'))

####################################################################################################################

def mini_menu(update,context):
    keyboard = [
        
        [InlineKeyboardButton("🍳🥞Desayuno🥯🥪", callback_data='desayuno')],
        [InlineKeyboardButton("🍝🍲Gourmet 🍱🍛", callback_data='gourmet')],
        
        [InlineKeyboardButton("🍔🍟Chatarra🍕🌯", callback_data='chatarra')],
        [InlineKeyboardButton("🧁🎂 Dulces 🍪🍩", callback_data='postre')]
        
    ]
    
    return keyboard

def second_menu(update,context):
    keyboard = [
        
        [InlineKeyboardButton("🍔🍟Combos🍪🥤", callback_data='combo')],
        [InlineKeyboardButton("🍤🥗Pasapalos 🧀🍾", callback_data='pasapalo')],
        [InlineKeyboardButton("🎂🍮Cumpleaños🥧🥮", callback_data='cumple')]
        
    ]
    
    return keyboard
#######################################################################################
# def start(update,context):
    
#     keyboard = [
        
#         [InlineKeyboardButton("🍔🍟Combos🍪🥤", callback_data='perro')]
  
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     update.message.reply_text('Hola '+str(update.message.chat.username)+'''Soy un Bot que trae ofertas de difrentes restaurantes en Valencia. 
#     Si quieres Mas selecciona /menu
#     Mayor Informacion de este Bot /soporte''', reply_markup=reply_markup)
############################################################################################

def start(update, context):

    keyboard = mini_menu(update,context)
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Hola '+'**'+str(update.message.chat.username)+'**'+''' Soy un Bot que trae ofertas de difrentes restaurantes en Valencia. 
    Si quieres Mas selecciona /menu
    Mayor Informacion de este Bot /soporte''', reply_markup=reply_markup)
    
def clasificacion_data(data, columna, seleccion):
        
    temp = data[data[columna]==seleccion]
    ix = list(temp.index)
    random.shuffle(ix)
    return ix, temp

def next_fun( update, context, 
                        x, temp, final ):
    
    
    ruta = 'ig_scrapper/database/images/'
    url_ig = 'https://www.instagram.com' + str(temp['user url'][x])
    

    if x == final:

        keyboard = mini_menu(update,context)
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.callback_query.message.reply_text('Ups😵, por ahora mi data es limitada😓', reply_markup=reply_markup)

    else:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo = open( ruta + str(temp['img name'][x]),'rb'))
        
        if temp['ws'][x] is False:
            keyboard = [
                
            [InlineKeyboardButton("Instagram", url=url_ig)],

            [InlineKeyboardButton("⏹Menu", callback_data='menu_'),
             InlineKeyboardButton("Siguiente▶️", callback_data='next_fun')]
                
            ]
        else:
            url_ws = 'https://api.whatsapp.com/send?phone='+ str(temp['ws'][x]) +'&text=Hola,%20Te%20encontre%20gracias%20Offer_Eat%20Telegram'
            keyboard = [
                    
            [InlineKeyboardButton("Whatsapp", url=url_ws),
            InlineKeyboardButton("Instagram", url=url_ig)],

            [InlineKeyboardButton("⏹Menu", callback_data='menu_'),
             InlineKeyboardButton("Siguiente▶️", callback_data='next_fun')]
                    
            ]
            
        reply_markup = InlineKeyboardMarkup(keyboard)

        # some Items doesn't have content
        if temp['content'][x] is False:
            update.callback_query.message.reply_text('Cuenta: '+ str(temp['user name'][x]), reply_markup=reply_markup)
        else:
            update.callback_query.message.reply_text('Cuenta: '+ str(temp['user name'][x]) + '\n' + temp['content'][x], reply_markup=reply_markup)
    
    

def post_fun(update,context, data, fd):

    ix, temp = clasificacion_data(data, fd[0], fd[1])
    
    final = ix[-1]
    x = iter(ix)
    next_fun(update, context, 
                        next(x), temp, final)
    print('next func cumplida')
    return x, temp, final
   


def post(update, context):
    
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open( 'ig_scrapper/database/images/image0.jpg','rb'))
    update.message.reply_text(data['content'][0])
    
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo = data['img url'][0])
    #  '\n <a href="t.me/telegram">t.me/telegram</a>'

def soporte(update, context):
    
    update.message.reply_text('''Este Bot esta en Version Beta, la idea simplificar la busqueda de restaurantes en Valencia.
    Desarrolado por Juan Vicente ventrone
    si deseas contactar a mi creador: https://t.me/JVentrone''')
    
def menu(update, context):
    
    k_1 = mini_menu(update,context)
    k_2 = second_menu(update,context)

    keyboard = k_1 + k_2
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        update.message.reply_text('Para Mayor Informacion /soporte', reply_markup=reply_markup)
    except:
        update.callback_query.message.reply_text('Para Mayor Informacion /soporte', reply_markup=reply_markup)

# This is bad, but it's just a propotype after, I will Fix this Chorizo!

def progresivo(update,context, x, temp, final):
    print("entramos")
    
    next_fun(next(x))

def desayuno(update, context):

    x, temp, final = post_fun(update,context, data, fd.desayuno)

    return x = x
        
        # next_fun(next(x))
    
def gourmet(update, context):   post_fun(update,context,data, fd.gourmet)
def gourmet(update, context):   post_fun(update,context,data, fd.gourmet)
def chatarra(update, context):  post_fun(update,context,data, fd.chatarra)
def postre(update, context):    post_fun(update,context,data, fd.postre)
def combo(update, context):     post_fun(update,context,data, fd.combo)
def pasapalo(update, context):  post_fun(update,context,data, fd.pasapalo)
def cumple(update, context):    post_fun(update,context,data, fd.cumple)




def main():
   
   
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1203014270:AAEcmANbEwlLCtDqCW_xogdgUMU92xh9cxc", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("soporte", soporte))
    
    #  Bottons Commander 
    dp.add_handler(CallbackQueryHandler(progresivo, pattern='^next$'))
    dp.add_handler(CallbackQueryHandler(desayuno, pattern='^desayuno$'))
    dp.add_handler(CallbackQueryHandler(gourmet,  pattern='^gourmet$'))
    dp.add_handler(CallbackQueryHandler(postre,   pattern='^postre$'))
    dp.add_handler(CallbackQueryHandler(chatarra, pattern='^chatarra$'))
    dp.add_handler(CallbackQueryHandler(combo,    pattern='^combo$'))
    dp.add_handler(CallbackQueryHandler(cumple,   pattern='^cumple$'))
    dp.add_handler(CallbackQueryHandler(pasapalo, pattern='^pasapalo$'))
    dp.add_handler(CallbackQueryHandler(menu,     pattern='^menu_$'))
    
    # dp.add_handler(CallbackQueryHandler(prueba, pattern='^perro$'))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    


if __name__ == '__main__':
    main()

