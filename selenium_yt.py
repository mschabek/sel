# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 13:59:38 2023

@author: user
"""

import time
import json
import random
from clint.textui import colored
import openai
import undetected_chromedriver as uc
# https://pypi.org/project/undetected-chromedriver/
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

HOME_DIR = r'C:\Users\user\Dysk Google\py'
PROFILE_DIR = r'C:\Users\user\AppData\Local\Google\Chrome\User Data\SProf2'
KEY = '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'


openai.api_key = KEY
prompt = """
Please generate user data according to following format. User name should be long and contain only words - not names.
Password should be long, contain letters, number and special characters.
Return only data for one user.

{
    "data": {
        "surname": "Jake",
        "name": "Stanley",
        "username": "StarryNightfallChaser87"
        "password": "sdk@i172$61kjsj8!"
    }
}
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo"
    ,messages = [
        {'role': 'user', 'content': prompt}
      ]
    ,temperature=0.1
    )

raw_response = response['choices'][0]['message']['content']
raw_response = raw_response.replace('\n', '').replace(' ', '')
user = json.loads(raw_response)


options = uc.ChromeOptions()
options.user_data_dir = PROFILE_DIR
options.add_argument('--disable-popup-blocking')
driver = uc.Chrome(use_subprocess=True, options=options)
driver.get('https://www.google.com/intl/pl/gmail/about/')
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/header/div/div/div/a[3]/span[2]').click()
time.sleep(2)

# Filling up form with user registration
driver.find_element(By.NAME, 'firstName').send_keys(user['data']['surname'])
driver.find_element(By.NAME, 'lastName').send_keys(user['data']['name'])
driver.find_element(By.NAME, 'Username').send_keys(user['data']['username'])
driver.find_element(By.NAME, 'Passwd').send_keys(user['data']['password'])
driver.find_element(By.NAME, 'ConfirmPasswd').send_keys(user['data']['password'])
# Confirmation
driver.find_element(By.XPATH, '//*[@id="accountDetailsNext"]/div/button').click()


# Switching to new tab with web page that receives sms confirmations
driver.execute_script('''window.open("https://anonymsms.com/gmail/","_blank");''')
time.sleep(2)
window_before = driver.window_handles[0]
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
numbers = driver.find_elements(By.CLASS_NAME, 'sms-card')
numbers_uk = [n for n in numbers if n.find_element(By.TAG_NAME, 'h4').text == 'United Kingdom']
number = random.choice(numbers_uk)
number.find_element(By.TAG_NAME, 'a').click()

len(numbers_uk)






driver.switch_to.window()



driver.quit()


user = {
    'surname': 'Jake',
    'name': 'Stanley',
    'username': 'StarryNightfallChaser87'
    'password': 'sdk@i172$61kjsj8!'
}

{'data': {
        'surname': 'Jake',
        'name': 'Stanley',
        'username': 'StarryNightfallChaser87'
        'password': 'sdk@i172$61kjsj8!'
    }
}


