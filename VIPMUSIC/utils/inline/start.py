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
                text=" ꧁𓊈𒆜𝐀𝐝𝐝 𝐦𝐞 𝐛𝐚𝐛𝐲𒆜𓊉꧂",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="꧁𓊈𒆜𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐂𝐡𝐚𝐧𝐧𝐞𝐥𒆜𓊉꧂", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="• 𒆜𝐂𝐨𝐦𝐦𝐚𝐧𝐝𒆜 •", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons
