#!/usr/bin/env python
# coding: utf-8
import os
import discord

import requests
import pymysql
import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import pymysql
import config
from sqlalchemy import create_engine
import user_functions as ufs
#to run the server
#from flask import Flask
#app = Flask(__name__)

headers = {"user-agent": config.USER_AGENT}
#resp = requests.get(URL, headers=headers)

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    '''
	params
	greeting message for a member joined
	'''
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    '''
	params
	message: message object received from user
	return : custom responses based on message
	'''
    if 'hi'==message.content.lower() and message.author!=client.user:
        await message.channel.send(f'Hey {message.author}, 🎈🎉')
    elif (message.content.lower()).startswith("!google") and message.author!=client.user:
        rurl = 'https://google.com/search?'
        rparams = {'q':(message.content).split("!google ")[1]}
        ufs.send_to_mysql(rparams['q'],message.author)
        await message.channel.send(str(ufs.get_top_links((requests.get(url=rurl,params = rparams, headers=headers)))))
    elif message.author!=client.user:
        await message.channel.send(f'Please choose options carefully 1. type hi, 2. type a search string followed by !google')


if __name__=="__main__":
    client.run(config.DISCORD_TOKEN)



# In[15]:


#client.close()

