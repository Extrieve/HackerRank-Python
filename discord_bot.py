import os
import discord
import requests
import json
import numpy as np
import datetime
import youtube_dl
import asyncio
from keep_running import keep_alive
from replit import db
from discord.utils import get
from discord.ext import commands
from datetime import date


client = discord.Client()
intents = discord.Intents.default()
intents.members = True

memelist = np.array(['https://imgur.com/ST9RRdZ', 'https://imgur.com/YOFy6O2', 'https://imgur.com/NHJscWK',
                    'https://imgur.com/AQrKLHS', 'https://imgur.com/T2kmXqQ', 'https://imgur.com/xSrY6F3', 'https://imgur.com/NfFlB1a'])

greats = np.array(['https://cdn.discordapp.com/attachments/193188992857014272/859280267352080384/e3012c5d489016f804b00696a7b0427e.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/859163415079813130/Junkiesbeseethinginthecoments_8d0f7dc9b13e41603fa14fb38bc8bb73.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/858198346844864562/Whatarethepurposeofthesecomicsjustcirclejerk_ea8428881b521b3e489f5516fc48f0d9.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/845385715427704862/Depressedrook_49d925_8440415.mp4', 'https://discord.com/channels/193188992857014272/193188992857014272/840789509532024833', 'https://cdn.discordapp.com/attachments/193188992857014272/824357641048162334/1fb7394de568f412c32e28ef6f63f86c.mp4', 'https://cdn.discordapp.com/attachments/595792876873580546/857081275193491517/video0-143.mp4', 'https://cdn.discordapp.com/attachments/787867027775029259/852957245804249099/video0-18.mp4', 'https://cdn.discordapp.com/attachments/386718408982528000/854385108295483442/video0.mov', 'https://cdn.discordapp.com/attachments/564169696547700746/854191093830516786/IM_GOING_TO_KILL_CHAOS.mp4',
                  'https://cdn.discordapp.com/attachments/825060471937040415/833469538108178442/sus.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/860225401703628820/qwe.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/856647303476805673/a_tu_casa.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/850526888421097502/video_1.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/850140189178200094/xdd.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/847901681777377281/getfvid_191184229_503335914218882_4166493292746332674_n.mp4', 'https://cdn.discordapp.com/attachments/715909144267456543/773793957146263582/123289186_364189861337254_4649832349965682829_n.mp4', 'https://cdn.discordapp.com/attachments/729055475445923964/759092722627117056/AngryChineseGuy.mov', 'https://cdn.discordapp.com/attachments/228646713026543618/861732683452776488/mzl2q7QxGDf8qbYDftcg_02_e908eaa7b460ecbf27ba255aca6d7fa8_video.mp4', 'https://2eu.funnyjunk.com/movies/Boom_7648b0_7820344.mp4', 'https://cdn.discordapp.com/attachments/193188992857014272/583096390964740106/meandtheboys.mp4'])

dota = ['https://cdn.discordapp.com/attachments/862790378925850624/867206248469757982/479019.mp4',
        'https://cdn.discordapp.com/attachments/222852560422174720/861740384336740363/DOTA_2_RAGE_-_PERUANO_Y_VENEZOLANO_ENOJADOS__.mp4']

miercoles = [
    'https://cdn.discordapp.com/attachments/862790378925850624/867642282203414528/5n5dibawgvd61.png']

jueves = ['https://tenor.com/view/asuka-feliz-jueves-running-happy-thursday-gif-16469364',
          'https://cdn.discordapp.com/attachments/862790378925850624/867203979996954684/feliz_jueves.mp4']

viernes = [
    'https://cdn.discordapp.com/attachments/193188992857014272/762724813147209788/hapifr.mp4']


# Return from the api
def get_quote():
  # Get Api
  response = requests.get('https://animechan.vercel.app/api/random')
  # Transform into json
  json_data = json.loads(response.text)
  quote = json_data['quote'] + ' | Character: ' + \
      json_data['character'] + ' | Series: ' + json_data['anime']
  return quote


def get_anime():
  # Get API
  response = requests.get('https://api.jikan.moe/v3')


def get_day():
  week = ["Lunes", "Martes", "Miercoles",
          "Jueves", "Viernes", "Sabado", "Domingo"]
  day = str(date.today()).split('-')
  day = [int(x) for x in day]
  week_num = datetime.date(day[0], day[1], day[2]).weekday()
  return week[week_num]


# Registering an event
@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(msg):

  if msg.author == client.user:
    return

  if 'Ans' in str(msg.author):
    if 'pi' in msg.content:
      await msg.channel.send('Tu vieja ma ni to')
    elif 'dota' in msg.content.lower():
      randnum = np.random.randint(0, len(dota))
      await msg.channel.send(dota[randnum])

  if 'Renato' in str(msg.author):
    if 'twitter.com' in msg.content:
      await msg.channel.send('Formatea bien tu meme csm')

  # Check if the msg starts with a command
  if msg.content.startswith('~weaboo'):
    quote = get_quote()
    await msg.channel.send(quote)

  if msg.content.startswith('~ogmeme'):
    randnum = np.random.randint(0, len(memelist))
    await msg.channel.send(memelist[randnum])

  if msg.content.startswith('~goodShit'):
    randnum = np.random.randint(0, len(greats))
    await msg.channel.send(greats[randnum])

  if msg.content.startswith('~day'):
    day = get_day()
    if(day.lower() == 'miercoles'):
      randnum = np.random.randint(0, len(miercoles))
      await msg.channel.send(f"_It is Wednesday my dudes._ Hang in there sailor~\n{miercoles[randnum]}")
    elif(day.lower() == 'jueves'):
      randnum = np.random.randint(0, len(jueves))
      await msg.channel.send(f"Feliz *{day}* gettin' close :ricardo:\n{jueves[randnum]}")
    elif(day.lower() == 'viernes'):
      randnum = np.random.randint(0, len(viernes))
      await msg.channel.send(f'Feliz *{day}*, you made it :yeehaw:\n{viernes[randnum]}')
    else:
      await msg.channel.send(f'Feliz *{day}*\nEsperabas algo mas putita?')

  if msg.content.startswith('~help'):
    await msg.channel.send(f'List of Commands(~): \nogmeme\ngoodShit\nday\nweaboo')


async def on_member_join(self, member):
  guild = member.guild
  role = get(message.server.roles, name='Normies')
  if guild.system_channel is not None:
      await member.add_roles(role)

# Run the bot, use environment variable to hide token.
keep_alive()
client.run(os.environ['bot_token'])
