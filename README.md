# alert-bot

### receiver
простой flask сервер слушает 5000 порт, получает josn от alertmanager 
парсит и отправляет сообщения в чаты 
отправка в телеграм через прокси сервер

### bot
комманды:
```
/getchatid - возвращает чат id
```

### сборка докер образа
```
make receiver-image
make bot-image
```



#### конфигурируется через env
```
$ cat env.sh
BOT_TOKEN=
SOCKS5_PROXY=
SOCKS5_PROXY_PORT=
SOCKS5_USER=
SOCKS5_PASSWORD=
```
