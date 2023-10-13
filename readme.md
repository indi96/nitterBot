# NitterBot for Telegram

This repository provides a sample implementation of a telegram bot that can convert https://twitter.com and https://twitter.com links to https://nitter.net/ links.

## Running

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) library.

```bash
pip install pyTelegramBotAPI
```

2. Replace the *InsertTokenHere* with your custom [telegram bot token](https://www.loginradius.com/blog/engineering/how-to-make-telegram-bot/#making-our-telegram-chatbot) in the line ```bot = telebot.TeleBot('InsertTokenHere', parse_mode=None)``` 

