# Discord Bot

---

The following code guides you through making a simple discord bot 

using [Python](https://python.org/) and [Discord.py](https://discordpy.readthedocs.io/en/latest/index.html).

# Discord Developer Portal

---

In order to be able to code a discord bot, you will have to create a bot

on the [Discord Developer Portal](https://discord.com/developers/applications). Log in with your discord account

and create a new application. Now choose that application and go 

to the bot section and create a new bot.

# Discord.py

---

### Installation

Open a new terminal and type the followig:

Windows: `pip install discord.py` or `py -m pip install discord.py`

Linux: `pip3 install discord.py`

---

### Creating your bot

```py
import discord


client = discord.Client()
```

As you can see above we are importing discord.py in the first line and

creating a client instance on the third line. The client object represents 

our bot. All commands we gonna create will be connected with it.

```py
@client.event
async def on_message(message):
    """This function is an event

        An event gets called when something happens.
        This event (on_message) gets called when the 
        bot receives a message (in guilds, dm's & 
        group chats). Discord.py automatically 
        passes a message object to this function,
        represented by the 'message' parameter.
        The message object represents the message
        which got received. 
    """
    # If the author of the message is the bot itself
    if message.author == client.user:
        return None
    # If the message doesn't start with the prefix '?'
    if not message.content.startswith('?'):
        return None
    # Slicing out the prefix to retrieve the command
    command = message.content.lower().split()[0][1:]

    # A basic ping command
    if command == 'ping':
        await message.channel.send('Pong')
```

Now where we defined an event its time to bring our bot online and 

see how it works.

```py
# This will run your bot using the bot token from
# discord developer portal. This code snippet should
# be on the last line of your file since its starts
# a never ending loop, so code written under it 
# will never get executed
client.run("bot_token")
```

---

### Documentation

You can find the discord.py documentation [here](https://discordpy.readthedocs.io/en/latest/api.html).

---

# Hosting your Bot

I guess that you don't wanna host your bot from your computer all the time. You can host your bot for freeon [Heruko](https://www.heroku.com). Create an account on heroku and create an application. Make an private repo on github and upload your script along with a "Procfile" and a "requirements.txt". You can find an example in this repo. Go to your heroku application and connect it with your github repo. Then upload it on heroku. After a short time you should be able to host your bot.
