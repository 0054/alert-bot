import os
import sys

config = {}

config['chats'] = dict()
try:
    config['token'] = os.environ['BOT_TOKEN']
    for env in os.environ:
        if "BOT_CHAT" in env:
            chat_name = "_".join(str(env).split("_")[2:]).lower()
            chat_id = os.environ[env]
            config['chats'][chat_name] = chat_id
except KeyError as e:
    print('Please set the environment variable ' + str(e))
    sys.exit(1)
