import discord
from discord.ext import commands
import os
from ai import get_class

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='$', intents=intents)

SAVE_DIRECTORY = "saved_images"
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command(name="saveimage")
async def save_image(ctx):
    attachments = ctx.message.attachments

    if not attachments:
        await ctx.send("❌ Tidak ada gambar yang dilampirkan. Silakan lampirkan gambar dan jalankan `!saveimage`.")
        return

    for attachment in attachments:
        if attachment.content_type and attachment.content_type.startswith("image/"):
            save_path = os.path.join(SAVE_DIRECTORY, attachment.filename)
            await attachment.save(save_path)
            await ctx.send(f"✅ Gambar `{attachment.filename}` telah disimpan di `{save_path}`.")

            result = get_class(save_path)

            await ctx.send(f"Gamber yang anda kirim adalah `{result}`.")
        else:
            await ctx.send(f"⚠️ File `{attachment.filename}` bukan gambar dan tidak disimpan.")

bot.run("MTMyMzUyMzkxMzEwNzY0MDM4MQ.G71oFJ.Mg3HHxSK2AVgwefmzCjhxDrsnoS5AYjBjx-dHc")