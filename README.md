#8 Discord Bot

A simple discord bot using discord.py

## Discord.py
### Installation
Use: `pip install discord` to install discord.py
### Documentation 
[Official Website](https://discordpy.readthedocs.io/en/latest/#)

## Files
### Procfile and requirements.txt
These are required files if you wanna host your bot on heroku.
### Main.py
This is the main file containing the script of the bot. 

## Getting started
I'm assuming that you have already installed python on your machine. Otherwise download it [here](https://www.python.org)
### Creating a bot 
Go to the [Discord Developer Portal](https://discord.com/developers/) and create a application. 
Then open your application and go to the bot section and create a bot. The token will 
be important to run your bot. _Never_ share your bots token. 
### Inviting your bot
Go the *OAuth2* of your application. Click on the *bot* field and then click on all 
permissions your bot requires. After that copy the link and type it into your broswer.
Now invite your bot to your server.
### Running your bot
Get the token of your bot (on the bot developer page) and past it into the variable "TOKEN" found in main.py 
Now simple run the script.
### Hosting 
I guess that you don't wanna host your bot from your computer all the time. You can host your bot for free
on [HEROKU](https://www.heroku.com). Create an account on heroku and create an application. 
Make an private repo on github and upload your script along with a "Procfile" and a "requirements.txt". You 
can find an example in this repo. Go to your heroku application and connect it with your github repo. Then 
upload it on heroku. After a short time you should be able to host your bot.
