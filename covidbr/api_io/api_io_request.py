#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################
## author: Reinan Br. ##
## date: 25/06/2021   ##
########################

##importando bibliotecas##
#from sys import ps1
from mechanicalsoup import browser
import requests
from covidbr.api_io.browser_slam import load_cookies, save_cookies
import os 
import pandas as pd
from covidbr.log import date_base
import mechanicalsoup
from covidbr.log import log
from bs4 import BeautifulSoup as bs

br = mechanicalsoup.StatefulBrowser()

userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'
path_cache_dir = '.cache/'


def login_io(user:str,password:str,url:str,browser:br=br,path_cookies:str='.cookies'):
    br = browser
    br.open(url)
    #log(f'sendding login [name:{user}, password: {password}] to site...')
    
    br.select_form()
    br['username'] = user
    br['password'] = password
    #br.launch_browser()
    log('Sendded login!')
    
    res = br.submit_selected()
    if not ('tente novamente' in str(res.content)):
        
        log('Login aceito!')
        save_cookies(browser=br,path_cookies=path_cookies)
        return br
    else:
        print("Login incorrect!")
        raise Exception(f'login required is incorrect or blocked')
        

def get_data_covid(city:str,state:str) -> str:
    br = mechanicalsoup.StatefulBrowser()
    log('modificando os agentes')
    br.session.headers = {"User-Agent":userAgent} #
    br.session.headers.update({"User-Agent":userAgent })
    log('abrindo site...')
    url = (f'https://brasil.io/dataset/covid19/caso_full/?state={state}&city={city}&format=csv')
    path_cookies = path_cache_dir+'/cookies_change'
    if (os.path.isfile(path_cookies)):
        load_cookies(browser=br,path_cookies=path_cookies)
    else:
        if os.path.isdir('.cache'):
            pass
        else:
            os.system('mkdir .cache')
    res = br.get(url)
    # error verification
    res.raise_for_status()
    if not ("entrar" in str(res.content)):
        log('ok!')
        html_source = requests.get('https://brasil.io/dataset/covid19/caso_full/').text
        soup_html_io = bs(html_source,'html.parser')
        update_date_dataset = soup_html_io.find_all('p')[-1].text
        log(update_date_dataset)
        return res.content
    else:
        log('login required!')
        br = login_io(user='reinan912',password='imaginando912',url=(f'https://brasil.io/dataset/covid19/caso_full/?state={state}&city={city}&format=csv'),path_cookies=path_cookies)
        log('ok!')
        html_source = requests.get('https://brasil.io/dataset/covid19/caso_full/').text
        soup_html_io = bs(html_source,'html.parser')
        update_date_dataset = soup_html_io.find_all('p')[-1].text
        log(update_date_dataset)
        return res.content
