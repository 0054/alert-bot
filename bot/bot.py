#!/usr/bin/env python3
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackContext)
from config import config
import telegram
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def getID(update: Update, context: CallbackContext):
    # logger.info(f'{update.message.date} - Chat: {update.message.chat_id} User: {update.message.from_user} Message: {update.message.text}')
    userID = update.message.from_user.id
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your ID = {userID}')

def getChatID(update: Update, context: CallbackContext):
    # logger.info(f'{update.message.date} - Chat: {update.message.chat_id} User: {update.message.from_user} Message: {update.message.text}')
    chatID = update.effective_chat.id
    context.bot.send_message(chat_id=chatID, text=f'Chat id = {chatID}')

def help(update: Update, context: CallbackContext):
    # logger.info(f'{update.message.date} - Chat: {update.message.chat_id} User: {update.message.from_user} Message: {update.message.text}')
    help = 'usage:\n/getid - return your telegram id\n/getchatid - return chat id'
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)

def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # строка с конфигом прокси сервера
    # updater = Updater(config.TOKEN, use_context=True, request_kwargs=config.REQUEST_KWARGS)
    updater = Updater(config['token'], use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.update.channel_post & Filters.text('/getchatid'), getChatID))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("getid", getID))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

