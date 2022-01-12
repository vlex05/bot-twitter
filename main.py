import tweepy
import time
import json
import requests
import pandas as pd
import cloudscraper
from tweet_texte import tweet_texte
from image_ens import image_ens
from reply_owner import reply_owner
from PIL import Image, ImageDraw, ImageFont
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from  keep_alive import keep_alive
import warnings
warnings.filterwarnings('ignore')

consumer_key = "xxYuoCr2RU0Xqx9bCnrCwsbmb"
consumer_secret = "oJh1ECv07k7rIiFC6VGj7ooSc2Uss5MrpYN9YrDiUUSxqQ3NsN"
access_token = "1399226488927498245-ZthLSAtbTOgnj3wcPzZBFoLSu9BOrD"
access_token_secret = "QRYPECqlvSAojDasRnW7QMjJpRbU4wT8aAkIFBfB6WI6C"

def WhaleTrackerENS(): 
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)  
    while True:   
        try:    
            #initialise la conexion à twitter.
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)

            #récupère le fichier .json de 'ens', le nom de domaine de la dernière vente & le nom de domaine de la dernière verif.

            url = "https://api.opensea.io/api/v1/assets?order_by=sale_date&order_direction=desc&offset=0&limit=50&collection=ens"
            json_url = json.loads(requests.request("GET", url).text)
            eth_domain = json_url['assets'][0]['name']
            last_eth_domain = pd.read_csv('WhaleTrackerEns/last_ens_name.csv').drop('Unnamed: 0',axis=1)

            #on continue si le nom de domaine =/= du dernier nom de domaine verifié.
            if eth_domain != last_eth_domain['last_ens_name'][0]:
                last_eth_domain['last_ens_name'][0] = eth_domain
                last_eth_domain.to_csv('WhaleTrackerEns/last_ens_name.csv')
                eth_price = int(json_url['assets'][0]['last_sale']['total_price'])/1000000000000000000

                # si le prix/eth > 0.5 récupère les données de la transaction.
                if eth_price > 0.5:
                    usd_price = round(float(json_url['assets'][0]['last_sale']['payment_token']['usd_price']) * (int(json_url['assets'][0]['last_sale']['total_price'])/1000000000000000000),2)
                    actual_owner = json_url['assets'][0]['owner']['address'][:8]
                    transaction_hash = json_url['assets'][0]['last_sale']['transaction']['transaction_hash']

                    url = 'https://etherscan.io/tx/'+transaction_hash
                    scraper = cloudscraper.create_scraper()
                    message = scraper.get(url).text 

                    before_owner = message[message.find('</span></a><span class=\'text-secondary mr-1 d-inline-block\'>From</span><span class=\' hash-tag text-truncate mr-1\'><a href=\'/address/')+len('</span></a><span class=\'text-secondary mr-1 d-inline-block\'>From</span><span class=\' hash-tag text-truncate mr-1\'><a href=\'/address/'):message.find('</span></a><span class=\'text-secondary mr-1 d-inline-block\'>From</span><span class=\' hash-tag text-truncate mr-1\'><a href=\'/address/')+len('</span></a><span class=\'text-secondary mr-1 d-inline-block\'>From</span><span class=\' hash-tag text-truncate mr-1\'><a href=\'/address/')+8]

                    tweet_text = tweet_texte(eth_price, last_eth_domain,eth_domain,usd_price,actual_owner,before_owner,json_url)

                    print('tweet')
                    post_result = image_ens(eth_domain,tweet_text,api)
                    
                    reply_owner(json_url,driver,api,post_result)
                else:
                    print('rien de nouveau')
            else:
                print('rien de nouveau')
            time.sleep(120)
        except:
          print('erreur !')
          time.sleep(30)
          pass
keep_alive()
WhaleTrackerENS()
