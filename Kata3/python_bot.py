'''Para comunicarnos con telegram. manjeador de comandos = CommandHandler'''
from telegram.ext import Updater, CommandHandler


def main():
    # el token se lo pedimos el bot father de telegram
    updater = Updater(token=open("Kata3/token.txt").read(), use_context=True)
    # reparte el trabajo entre todos los manejadores (handler) start en mi caso
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repite", repite))
    updater.dispatcher.add_handler(CommandHandler("suma", suma))
    # Empezamos apedir notificaciones en telegram
    updater.start_polling()
    # Capturamos señales de parada
    updater.idle()

def start(update, context):
    # respondemos al comando start
    update.message.reply_text("Hello! I'm a bot.")

def repite(update, context):
    # respondemos al comando repite
    update.message.reply_text(update.message.text)

def suma(update, context):
    # respondemos al comando suma
    # nuestros argumentos son args = [2, 2]
    result = int(context.args[0]) + int(context.args[1])
    update.message.reply_text(f"El resultado es {result}")


main()