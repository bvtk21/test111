import telegram
import logging
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time

# Set up the logging module
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Set up the OpenAI API key
openai.api_key = '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'

# Define the start command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the OpenAI bot!")

# Define the message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please wait while I process your request...")
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="davinci",
        prompt=update.message.text,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    # Send the response back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)
    time.sleep(3)

# Set up the Telegram bot
def main():
    updater = Updater(token='6144931878:AAHu2guR3u_4aIYdPoWScrVFZtLWi8dVDPw', use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers for the start command and messages
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()
