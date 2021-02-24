from pyrogram import (
    Client,
    filters
    )

MESSAGE = """
Hey yo!, You want to use me In Group ?\nTell this
in @NexaBots !!\nCurrently Leaving 👋
"""


@Client.on_message(filters.group)
async def leave(client, message):
    await message.reply_text(MESSAGE)
    await message.chat.leave()
