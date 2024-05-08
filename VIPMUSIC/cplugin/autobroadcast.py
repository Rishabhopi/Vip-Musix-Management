import asyncio
import datetime
from pyrogram import Client
from config import START_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
from typing import Dict, List, Union
from VIPMUSIC.utils.database import get_served_chats_clone
from VIPMUSIC import userbot
from VIPMUSIC.core.mongo import mongodb, pymongodb

AUTO_GCAST = True

START_IMG_URLS = "https://graph.org/file/8497b3052bf3da8137d2a.jpg"

MESSAGES = f"""
ᴛɪʀᴇᴅ ᴏғ ᴘʀᴏᴍᴏᴛɪᴏɴᴀʟ ᴀᴅᴠᴇʀᴛɪꜱᴇᴍᴇɴᴛ ᴘᴏꜱᴛꜱ ᴏɴ ᴏᴛʜᴇʀ ʙᴏᴛꜱ?

ᴛʀʏ - 🐾 ˹ʙᴜɢ ✘ ϻʊsɪx ˼ 
↳ @BuG_Musix_Bot   🐾

↬ ᴀᴅꜱ & ᴘʀᴏᴍᴏᴛɪᴏɴꜱ ғʀᴇᴇ.
↬ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜꜱɪᴄ ᴘʟᴀʏᴇʀ
↬ 24x7 ᴜᴘᴛɪᴍᴇ.
↬ ꜱᴜᴘᴘᴏʀᴛꜱ ᴍᴜʟᴛɪ-ʟᴀɴɢᴜᴀɢᴇ /  ᴀʀᴀʙɪᴄ - ʜɪɴᴅɪ - ᴘᴜɴᴊᴀʙɪ.
↬ ʟᴀɢ ꜰʀᴇᴇ

🔧 ᴠɪꜱɪᴛ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ 
↳ @Flames_xD  ғᴏʀ ᴍᴏʀᴇ !

**"""


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "• ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ •",
                url=f"https://t.me/Flames_xD",
            )
        ]
    ]
)

MESSAGE = f"""**ᴀᴅᴅ ~ @BuG_Musix_Bot ~  ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘꜱ 💞

🥀 ᴢᴇʀᴏ ᴅᴏᴡɴᴛɪᴍᴇ & ʟᴀɢꜰʀᴇᴇ ᴍᴜꜱɪᴄꜱ 🤍

/start"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "• ᴋɪᴅɴᴀᴘ ᴍᴇ ʙᴀʙʏ •",
                url=f"https://t.me/BuG_Musix_Bot?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""


async def send_message_to_chats(client: Client):
    try:
        chats = await get_served_chats_clone()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await client.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(
                        1
                    )  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_cbroadcast():
    # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats(client)
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(5)


# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:
    asyncio.create_task(continuous_cbroadcast())
