import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # スラッシュコマンドを全サーバーに同期
        await self.tree.sync()
        print("スラッシュコマンドが同期されました")

client = MyClient()

@client.event
async def on_ready():
    print(f'✅ Bot起動成功: {client.user}')

# /こんにちは コマンドの定義
@client.tree.command(name="こんにちは", description="Botがあいさつします")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"こんにちは、{interaction.user.mention}！")

# あなたのBotのトークンをここに貼り付けて
client.run("あなたのBotのトークン")
