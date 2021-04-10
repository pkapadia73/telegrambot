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
        
    
# chat_id = ["906332984","1101056134"]
token = "1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg"


b = 'https://api.telegram.org/bot1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg/getUpdates?offset=122028830'
z = json.loads(requests.get(b).content)
        
# reply = z['result'][-1]['message']['text']                  #TCS
chat_id = z['result'][-1]['message']['chat']['id']
update_id = z['result'][-1]['update_id']       #51
# update = z['result'][-2]['update_id']          #50

# y = stock_name.index(reply)                         #3238           


last_update_id = update_id


while True:        
    #CODE FOR GETTING UPDATES
    b = 'https://api.telegram.org/bot1771550068:AAFyaWVAzp_1rIlR2JJ3mIip5fOD1IpPXgg/getUpdates?offset=122028830'  
    z = json.loads(requests.get(b).content)    
    update_id = z['result'][-1]['update_id']
    reply = z['result'][-1]['message']['text']
              
    #CODE FOR WEBSCRAPING
    stock_name = sel.xpath('//span[@class="gld13 disin"]/a//text()').extract()   
    stock_price = sel.xpath('//td[4][@align="right"]/text()').extract()
    
    
    
    if last_update_id != update_id:
        reply = z['result'][last_update_id - update_id]['message']['text']
        y = stock_name.index(reply)
        chat_id = z['result'][last_update_id - update_id]['message']['chat']['id']

           
        #CODE FOR SENDING MESSAGES
        link = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}'.format(token,chat_id,stock_price[y])
        requests.get(link)
           
        last_update_id += 1
    
