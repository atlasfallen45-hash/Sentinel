import os
from dotenv import load_dotenv
import discord

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} está listo!')

client.run(TOKEN)
