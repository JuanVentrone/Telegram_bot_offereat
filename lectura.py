"""
    Ejemplo 1 - Este programa escribe por Terminal el contenido del ultimo mensaje
            que ha recibido el chatbot junto con el nombre del autor y la ID del chat.
 
    Escrito por Transductor
    www.robologs.net
"""
 
#Importar librerias
import json
import requests
 
#Variables para el Token y la URL del chatbot
TOKEN = "751988420:AAHrzn7RXWxVQQNha0tQUzyouE5lUcPde1g" #Cambialo por tu token
URL = "https://api.telegram.org/bot" + TOKEN + "/"
 
 
 
def update():
    #Llamar al metodo getUpdates del bot haciendo una peticion HTTPS (se obtiene una respuesta codificada)
    respuesta = requests.get(URL + "getUpdates")
 
    #Decodificar la respuesta recibida a formato UTF8 (se obtiene un string JSON)
    mensajes_js = respuesta.content.decode("utf8")
 
    #Convertir el string de JSON a un diccionario de Python
    mensajes_diccionario = json.loads(mensajes_js)
 
    #Devolver este diccionario
    return mensajes_diccionario
 
 
def leer_mensaje():
 
    #Llamar update() y guardar el diccionario con los mensajes recientes
    mensajes = update()
 
    #Calcular el indice del ultimo mensaje recibido
    indice = len(mensajes["result"])-1
 
    #Extraer el texto, nombre de la persona e id del último mensaje recibido
    texto = mensajes["result"][indice]["message"]["text"]
    persona = mensajes["result"][indice]["message"]["from"]["first_name"]
    id_chat = mensajes["result"][indice]["message"]["chat"]["id"]
 
    #Mostrar esta informacion por pantalla
    print(persona + " (id: " + str(id_chat) + ") ha escrito: " + texto)
 
 
#Llamar a la funcion "leer_mensaje()"
leer_mensaje()