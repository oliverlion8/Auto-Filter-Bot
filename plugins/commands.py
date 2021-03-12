#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from script import script

trojanzhex_IMG = "https://telegra.ph/file/b8067073614796fc36fe3.jpg"


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    try:
        await message.reply_photo( trojanzhex_IMG, )
            text=script.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("☘ ᴊᴏɪɴ ᴏᴜʀ ᴍʏ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ☘", url="https://t.me/hcf_chat")
                    ],
                    [
                        InlineKeyboardButton(
                            "👑 ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴋɪɴɢ 👑", url="https://t.me/AB_Nero")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    try:
        await message.reply_photo(
            text=script.HELP_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="start_data"),
                        InlineKeyboardButton("ABOUT", callback_data="about_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "👑 ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ᴋɪɴɢ 👑", url="https://t.me/AB_Nero")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    try:
        await message.reply_text(
            text=script.ABOUT_MSG,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("BACK", callback_data="help_data"),
                        InlineKeyboardButton("START", callback_data="start_data"),
                    ],
                    [
                        InlineKeyboardButton(
                            "SOURCE CODE", url="https://github.com/TroJanzHEX/Auto-Filter-Bot")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
    except:
        pass
