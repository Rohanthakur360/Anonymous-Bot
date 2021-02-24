from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **ANONYMOUS NEXA BOT.**\n
Just Forward me Some messages or
media and I will **Anonymize** that !!

Made with ❤️ by @NexaBotsUpdates
"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("⚜️ My Updates Channel ⚜️",
                          url="t.me/NexaBotsUpdates")],
    [InlineKeyboardButton("🔰 Dev 🔰",
                          url="t.me/Bruh_0x")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
