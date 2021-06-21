#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

if(os.path.isdir('config')):
    terminal = os.system
    print('apagando pasta config...')

    #apagando a pasta config
    terminal('rm config/*')
    terminal('rm config/log/*')
    terminal('rmdir config/log')
    terminal('rmdir config')

from instabot import Bot
#from instabot import InstaBot as 
bot = Bot()

username:str = 'gpftc_ifsertao'
password:str = 'imaginando912'

bot.login(username=username,password=password)#,use_cookie=True)
#print((bot.get_timeline_medias()))
#print(f'são {len(bot.followers)} seguidores no total')
bot.upload_photo(photo='sample-out.jpg',caption='apenas um teste em #python')
