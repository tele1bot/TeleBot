# Made for TeleBot
# Re-written by @its_xditya 
# Kangers kwwp the credits

#Made by @WhySooSerious
#From Nekos API

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="sologif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Solo GIF..```\n**It's Barely SFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/sologif")
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @KeikoSDbot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="cumgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Henti Cum GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
            await borg.send_message(chat, "/cumgif")
            response = await response
        except YouBlockedUserError:
              await event.reply("```Please unblock @KeikoSDbot and try again```")
              return
        if response.text.startswith("Forward"):
             await event.edit("```can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="ngif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Neko GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/ngif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="tickle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Tickle GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/tickle")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="feed"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Feeding GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/feed")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="bjgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Blow Job GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bjgif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
    #By @WhySooSerious

@borg.on(admin_cmd(pattern="analgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Anal GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bj")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="poke"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Poke GIF..```\n**Oh! It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/poke")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="pussygif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Pussy GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/pussygif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd(pattern="hentaigif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/hentaigif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd(pattern="classic"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Classic GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/classic")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="kuni"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Pussy Lick GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kuni")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="cuddle"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Cuddle GIF..```\n**WARNING : It's Really Kawaii**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/cuddle")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="titsgif"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding a Hentai Tits GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/titsgif")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#by @WhySooSerious
@borg.on(admin_cmd(pattern="smug"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Smug GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/smug")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
@borg.on(admin_cmd(pattern="baka"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an Anime Baka GIF..```\n**It's SFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/bj")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await event.delete()
                await borg.send_file(event.chat_id, response.message.media)

#By @WhySooSerious

@borg.on(admin_cmd(pattern="lesbian"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an A Hentai Lesbian GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/lesbian")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd(pattern="nsfwneko"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an A Hentai Neko GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/nekonsfw")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious

@borg.on(admin_cmd(pattern="kiss"))
async def _(event):
    if event.fwd_from:
        return
    chat = "@KeikoSDbot"
    await event.edit("```Finding an an Anime Kissing GIF..```\n**WARNING : It's NSFW**")
    async with borg.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
                await borg.send_message(chat, "/kiss")
                response = await response
            except YouBlockedUserError:
                await event.reply("```Please unblock @KeikoSDbot and try again```")
                return
            if response.text.startswith("Forward"):
                await event.edit("```can you kindly disable your forward privacy settings for good?```")
            else:
                await borg.send_file(event.chat_id, response.message.media)
#By @WhySooSerious
