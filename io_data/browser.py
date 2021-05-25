#nome = 
import requests as rq
#import mechanicalsoup as ms
#from bs4 import beautifulsoup as bs
import mechanicalsoup


def browser(url:str,headers:dict) -> object:
	userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'

	br = mechanicalsoup.StatefulBrowser()

	print('modificando os agentes')
	br.session.headers = {"User-Agent":userAgent} #
	br.session.headers.update({"User-Agent":userAgent }) 

	if headers['proxy']:
		br.session.proxies = {'https':headers['proxy']['https'],
							'http':headers['proxy']['http']
							} 

	return br

