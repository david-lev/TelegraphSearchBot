# Telegraph Search Bot

Many people use the [Telegra.ph](https://telegra.ph/) platform to write articles and guides In order to get a Instant View in Telegram apps.
This bot will let you to give your users a great tool to search among the articles you have created in your telegra.ph account.

## How to config?

- Clone this repository:

```
git clone https://github.com/david-lev/TelegraphSearchBot.git
```
- Install requirements:
```
pip3 install requirements.txt
```
- create ``config.ini`` file in [bot](/bot) folder.
- insert the folowing values into the [config](/bot/config.ini) file:
```
[pyrogram]
api_id = 123456
api_hash = 1ed37e2986541c7780cc7a1ed3ccgr09877

bot_token = 1463783971:AAhvhPOjegcpHV3nyVJC-XToLhecHNMPhhyo

[plugins]
root = bot

[telegraph]
access_token = e8200db69743a915f7c78c3799793Kbeec4e5a3a47fd7437073b42e7e
```
#### Telegram keys:
- the ``api_id`` & ``api_hash`` You can get from [my.telegram.org](https://my.telegram.org).
- ``bot_token`` you can get by create new bot on [BotFather](https://t.me/BotFather).
#### Telegra.ph Token:
to get ``access_token`` for your telegra.ph account go to [Telegraph Bot](https://t.me/telegraph), chosse your account and log into the browser.
in the addreess bar click on the lock icon > Cookies > ``edit.telegra.ph`` > Cookies > ``tph_token`` > Content. [here](https://telegra.ph/file/18ded40043d1f7a6a5a80.png) is an example.

### Strings
you can edit the bot strings (start message, buttons and more) by changing the values in [strings.py](bot/strings.py) file. there is also option to ignore from posts that start in spesific char, for posts that you dont want to appear in the search.

## How to run?
go to project directory:
```cd TelegraphSearchBot```

and run it:
```python3 main.py```


---
![]()
