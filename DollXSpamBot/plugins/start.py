
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from DollXSpamBot import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

DOLL_IMG = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/32e883a07287e1291a8ab.jpg"


Button = [
        [
        Button.url("Cʜᴀɴɴᴇʟ", "https://t.me/hey_villa"),
        Button.url("Sᴜᴘᴘᴏʀᴛ", "https://t.me/hey_villa")
        ],
        [
        Button.url("• Rᴇᴘᴏ •", "https://t.me/hey_villa")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={5730814680})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={5730814680})"
        creator = f"[༎ࠫ🫧⛧‌ٖٖٖٖٖٖٜٖٖٖ 𝐌͢ꝛ 𝐒𝐇𝐀𝐔𝐑𝐘𝐀༏͢𐏓ᥫᩣ●───♫▷](https://t.me/CutePagal)"
        DOLL_ON = f"""
ʜᴇʏ {mention},
ᴛʜɪs ɪs sʜᴀᴜʀʏᴀXsᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- {creator}!

ᴛʜɪs ʙᴏᴛ ɪs ꧁🇮🇳 🎀  𝑀𝒶𝒹𝑒 𝐼𝓃 𝐼𝓃𝒹𝒾𝒶  🎀 🇮🇳꧂

ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ:- {myOwner}

ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ:- {creator}

ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, DOLL_IMG, caption=DOLL_ON, buttons=Button)
