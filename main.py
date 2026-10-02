import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

print("Starting bot...")
print("TOKEN exists:", TOKEN is not None)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Bot Online! Logged in as {bot.user}")


@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("กรุณาเข้า Voice Channel ก่อน")
        return

    channel = ctx.author.voice.channel

    if ctx.voice_client:
        await ctx.send("Bot อยู่ในห้องแล้ว")
        return

    await channel.connect()
    await ctx.send(f"Bot เข้าห้อง {channel.name} แล้ว")


if not TOKEN:
    print("ERROR: TOKEN ไม่มีค่า")
else:
    bot.run(TOKEN)