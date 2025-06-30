import discord
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'ログイン成功: {bot.user}')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "ping":
        await message.channel.send("🏓 pong!")

bot.run(os.environ["TOKEN"])