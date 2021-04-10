#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:57:19 2021

@author: prerna
"""

from scrapy import Selector
import requests
import time
import json


url = 'https://www.moneycontrol.com/stocks/marketstats/nse-gainer/nifty-50_9/'
html = requests.get( url ).content
sel = Selector( text = html )
        
    
token = "1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg"


b = 'https://api.telegram.org/bot1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg/getUpdates?offset={}'.format(update_id - 3)
z = json.loads(requests.get(b).content)

update_id =  z['result'][-1]['update_id']
chat_id = z['result'][-1]['message']['chat']['id']
token = '1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg'
message_id =  z['result'][-1]['message']['message_id']

reply = z['result'][-1]['message']['text']
#y = stock_name.index(reply)

m = 'Stock not in list'

last_update_id = update_id

     
       
while True:
    b = 'https://api.telegram.org/bot1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg/getUpdates?offset={}'.format(update_id - 3)
    z = json.loads(requests.get(b).content)
    update_id =  z['result'][-1]['update_id']

    
    # while last_update_id != update_id:
    reply = z['result'][-1]['message']['text']
    
    chat_id = z['result'][-1]['message']['chat']['id']
    m = ['Stock not in list']

    if (reply in stock_name) and (last_update_id != update_id):                
        y = stock_name.index(reply)
        link = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token,chat_id,stock_price[y])
        requests.get(link)
        
        last_update_id += 1
        print (stock_price[y])
        
    elif last_update_id != update_id:               
        link = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token,chat_id,m)
        requests.get(link)
        last_update_id += 1
