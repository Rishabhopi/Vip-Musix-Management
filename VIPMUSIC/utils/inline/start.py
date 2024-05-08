from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="• ʜᴇʟᴩ •", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="• sᴇᴛᴛɪɴɢs •", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ •",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="• sᴜᴘᴘᴏʀᴛ •", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="• ᴄʜᴀɴɴᴇʟ •", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="• ᴄᴏᴍᴍᴀɴᴅs •", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
