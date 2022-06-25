#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from YukkiMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["S_B_99"],
                url=f"https://instagram.com/4wz.c?igshid=YmMyMTA2M2Y=",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    def sdd(call):	
	if call.data =='F1':
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("𝗹4", callback_data="F")
		B = types.InlineKeyboardButton("𝗹4", callback_data="F2")
		C = types.InlineKeyboardButton("𝗰7", callback_data="F3")
		D = types.InlineKeyboardButton("𝗰𝗼9", callback_data="F4")
		F = types.InlineKeyboardButton("𝖽𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𖠛", url='https://t.me/0')
		mas.add(A,B,C,D,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="r7unu4i",reply_markup=mas)		
		pass
	elif call.data =="F4":
		mas = types.InlineKeyboardMarkup(row_width=2)
		A = types.InlineKeyboardButton("9", callback_data="Dg")
		B = types.InlineKeyboardButton("9", callback_data="Dh")
		C = types.InlineKeyboardButton("𝗼9", callback_data="Do")
		D = types.InlineKeyboardButton("0", callback_data="Dy")
		H = types.InlineKeyboardButton("𝗺0", callback_data="Dm")
		G = types.InlineKeyboardButton("l", callback_data="Dr")		
		F = types.InlineKeyboardButton("4 ", callback_data="F1")
		mas.add(A,B,C,D,H,G,F)
		bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="𝐜𝐡𝐨𝐨𝐬𝐞 𝐨𝐧𝐞 𝐨𝐟 𝐭𝐡𝐞 𝐛𝐮𝐭𝐭𝐨𝐧𝐬 𝄵",reply_markup=mas)		
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_8"], callback_data="settings_back_helper"
            )
        ]
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                    )
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO and OWNER:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"{GITHUB_REPO}"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"{GITHUB_REPO}"
                    ),
                ]
            )
        if OWNER:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_7"], user_id=OWNER
                    ),
                ]
            )
    buttons.append(
        [InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")]
    )
    return buttons
