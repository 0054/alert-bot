import os
import sys

config = {}

config['chats'] = dict()
try:
    config['token'] = os.environ['BOT_TOKEN']
    # SOCKS5_PROXY = os.environ['SOCKS5_PROXY']
    # SOCKS5_PROXY_PORT = os.environ['SOCKS5_PROXY_PORT']
    # SOCKS5_USER = os.environ['SOCKS5_USER']
    # SOCKS5_PASSWORD = os.environ['SOCKS5_PASSWORD']
    for env in os.environ:
        if "BOT_CHAT" in env:
            chat_name = "_".join(str(env).split("_")[2:]).lower()
            chat_id = os.environ[env]
            config['chats'][chat_name] = chat_id
except KeyError as e:
    print('Please set the environment variable ' + str(e))
    sys.exit(1)


# REQUEST_KWARGS={
#         'proxy_url': f'socks5://{SOCKS5_PROXY}:{SOCKS5_PROXY_PORT}',
#         'urllib3_proxy_kwargs': {
#             'username': SOCKS5_USER,
#             'password': SOCKS5_PASSWORD,
#             }   
#         }


