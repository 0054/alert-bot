#!/usr/bin/env python3

from typing import Dict, NoReturn, List

import json
import telegram
from datetime import datetime
from flask import Flask, request, jsonify
from config import config

# эта часть нужна для подключения прокси
#from telegram.utils.request import Request
#ProxyRequest = Request(proxy_url=config.REQUEST_KWARGS['proxy_url'], urllib3_proxy_kwargs=config.REQUEST_KWARGS['urllib3_proxy_kwargs'])

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
app = Flask(__name__)


# def getChatID(update: Update, context: CallbackContext):
#     chatID = update.effective_chat.id
#     context.bot.send_message(chat_id=chatID, text=f'chat id = {chatID}')



# обработчик для alertmanager 
# парсит данные из alerManager
def reaction(data: Dict,  chat: str) -> NoReturn:
    message = prettyMessage(parseData(data))
    chat_id = config['chats'][chat]
    sendAlert(message, chat_id)

# принимает chat_id и сообщение и сразу отправляет 
def sendAlert(message: str, chat_id: str) -> NoReturn:
    bot = telegram.Bot(token=config['token'])
    bot.sendMessage(chat_id=chat_id, text=message)

# принимает json формата
# { "from": "Jenkins": "message": "сборка успешно прошла" }
# формирует сообщение from bla bla bla \n сообщение
# передаёт в sendAlert
def sendMessage(data: Dict, chat: str) -> NoReturn:
    message = data['message']
    fromMessage = data['from']
    alert = f'from: {fromMessage}\n{message}'
    sendAlert(alert, chat)


# делает из списка строки
def prettyMessage(data: List) -> str:
    return '\n'.join([' '.join(x) for x in data ])

# парсит сообщение из alermanager
# достаёт оттуда status, hostname, description
def parseData(data: Dict) -> List:
    alerts: Dict = data['alerts']
    messageList: List = [(alert['status'], alert['labels']['instance'], alert['annotations']['description']) for alert in alerts]
    return messageList


@app.route('/help')
def index():
    help = { '/receiver/<chat>': 'путь для alermanager <chat> заменить на название чата из списка chatList',
            'chatList': config['chats']
            }
    return jsonify(help)

@app.route('/receiver/<chat>', methods=['POST'])
def reveiver(chat: str):
    data = request.get_json()
    reaction(data, chat)
    return 'OK', 200

@app.route('/message/<chat>', methods=['POST'])
def message(chat: str):
    data = request.get_json()
    chat_id = config['chats'][chat]
    logger.info(f'data: {data}, chat_id: {chat_id}')
    sendMessage(data, chat_id)
    return 'OK', 200

@app.route('/raw/<chat>', methods=['POST'])
def raw(chat: str):
    data = request.get_json()
    chat_id = config['chats'][chat]
    logger.info(f'data: {data}, chat_id: {chat_id}')
    sendAlert(data, chat_id)
    return 'OK', 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
