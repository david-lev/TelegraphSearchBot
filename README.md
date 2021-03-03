# Telegraph Search Bot

Many people use the [Telegra.ph](https://telegra.ph/) platform to write articles and guides In order to get a [Instant View](https://instantview.telegram.org/) in Telegram apps.
This bot will let you to give your users a great tool to search among the articles you have created in your telegra.ph account.

- You can check out our bot [here](https://t.me/AndrotipsSearchBot).
<p float="left">
  <img src="https://telegra.ph/file/7c7dc172ab8816d1f9129.png" width="170" />
  <img src="https://telegra.ph/file/2efb80a844b5bfb11ad3f.png" width="150" /> 
</p>

## How to config?

- Clone this repository:

```
git clone https://github.com/david-lev/TelegraphSearchBot.git
```
- Install requirements (``pyrogram, telegraph, tgcrypto``):
```
pip3 install -r requirements.txt
```
- edit and insert the folowing values into the [config](/bot/config.ini) file:
```
[pyrogram]
api_id = 53**5287
api_hash = 1ed3*******0cc7a1ed***fcc77

bot_token = 1463783971:AAGuhvh****C-X**oxvHN**hhyo

[plugins]
root = bot

[telegraph]
access_token = e8200db697*****8c3791296f**0f77c4e5a***2e7e

[telegram]
bot_username = @YourBotUsername
```
#### Telegram keys:
- the ``api_id`` & ``api_hash`` You can get from [my.telegram.org](https://my.telegram.org).
- ``bot_token`` & ``bot_username`` you can get by create new bot on [BotFather](https://t.me/BotFather).
#### Telegra.ph Token:
to get ``access_token`` for your telegra.ph account go to [Telegraph Bot](https://t.me/telegraph), chosse your account and log into the browser.
in the addreess bar click on the lock icon > Cookies > ``edit.telegra.ph`` > Cookies > ``tph_token`` > Content. [here](https://telegra.ph/file/18ded40043d1f7a6a5a80.png) is an example.

### Strings
- You can change the bot view by editing the [Strings.py](bot/string.py) file. You can set an welcome message, channel credit, inline buttons and more. The default is in English but you can change if you want. dont delete the ``{}`` characters.
- There is a string named [char_ignore](https://github.com/david-lev/TelegraphSearchBot/blob/c6b803000f1b938c336064bd22ae0473ffe35075/bot/strings.py#L13) that sets to ignore any post whose title starts with the same character. This way you can hide or create new posts that do not appear in the general search (can be changed at any time.)

## How to run?
go to project directory:
```
cd TelegraphSearchBot
```
and run it:
```
python3 main.py
```
---
![]()
