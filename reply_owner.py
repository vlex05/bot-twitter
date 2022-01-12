from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def reply_owner(json_url,driver,api,post_result):
    try:
        driver.get('https://opensea.io/'+(json_url['assets'][0]['owner']['user']['username']))
        tweetos = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/main/div/div/div[1]/div[3]/div[4]/div[1]/a/div/div').text
        if tweetos[0] == '@':
            reply_text = ('Super sale 😊 !! Congratulations to the new owner '+tweetos+' of '+eth_domain+' .' )
            reply = api.update_status(status = reply_text, in_reply_to_status_id = post_result._json['id'] , auto_populate_reply_metadata=True)
        
        else:
            reply_text = ('Super sale 😊, congratulations ' +'@'+tweetos +' on our purchase!')
            reply = api.update_status(status = reply_text, in_reply_to_status_id = post_result._json['id'] , auto_populate_reply_metadata=True)
    except:
        print('pas de compte twitter')
        pass
