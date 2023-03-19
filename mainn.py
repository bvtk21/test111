from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from revChatGPT.V1 import Chatbot

chatbot = Chatbot(config={
    "email": "mokej48555@kaftee.com",
    "password": "defaulthing"
})

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот.")

def echo(update, context):
    prompt = update.message.text

    response = ""

    for data in chatbot.ask(prompt):
        response = data["message"]

    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def main():
    updater = Updater(token='5284088257:AAEk0boSkIvZy0RS55gWfV4GhJgxYXgBDSY', use_context=True)

    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
