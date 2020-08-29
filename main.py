import discord
from typing import List


bot = discord.Client()


PREFIX = "!"
TOKEN = "your_token"


@bot.event
async def on_ready():
    """This events gets triggered, once the bot is ready to perform
    """
    print("*" * 30)
    print(f"Logged in as {bot.user}")
    print("*" * 30)


@bot.event
async def on_message(message: discord.Message):
    """Every time a message gets send, this event triggers

    Parameters
    ----------
    message : discord.Message
        The message object which got send. This gets
        initialized by the library.
    """
    if message.author.bot:  # If the author is a bot
        return  # Leaving this function
    if not message.content.startswith(PREFIX):
        return
    
    # The command which got used in the message 
    command: str = message.content.lower().split()[0][len(PREFIX):]
    
    # A list containing all arguments passed by the user 
    args: List[str] = message.content.lower().split()[1:]
    
    # A common bot command
    if command == "ping":
        await message.channel.send(f"Pong...{round(bot.latency, 2)}ms")
        
    if command == "embed":
        embed = discord.Embed(  # This creates an embed object
            title="My first embed message",
            description="Yeah",
            color=discord.Color().dark_blue()
        )
        await message.channel.send(embed=embed)

bot.run(TOKEN)  # This runs the bot 