from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time
import random

options = Options()
options.headless = False;
options.add_argument("--disable-gpu");
options.add_argument("--ignore-certificate-errors-spki-list");
options.add_argument("--ignore-ssl-errors");
options.add_argument("--test-type");
options.add_argument("--no-default-browser-check");
options.add_argument("--ignore-certificate-errors");
options.add_argument("--allow-running-insecure-content");
options.add_argument("--window-size=1200,1100");

print ("""
    __    _____             _       _
    \ \  /  __ \           | |     | |
 _   \ \ | /  \/ __ _ _ __ | |_ ___| |__   __ _
| | | \ \| |    / _` | '_ \| __/ __| '_ \ / _` |
| |_| |\ \ \__/\ (_| | |_) | || (__| | | | (_| |
 \__,_| \_\____/\__,_| .__/ \__\___|_| |_|\__,_|
                     | |
                     |_|                        """)

with open('config.txt') as f:
  credentials = [x.strip().split(':') for x in f.readlines()]
  random.choice('config.txt')

for email,password in credentials:

    def main_function():
        driver = webdriver.Chrome(chrome_options=options)
        print ('Logging into Gmail...')
        driver.get('https://www.gmail.com')
        time.sleep(3)
        driver.find_element_by_id('identifierId').send_keys(email)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
        print ('Logged in as: '+ email)
        print ('----------------------------------')
        time.sleep(2)


        print ('Searching for Youtube videos...')
        driver.get('https://www.google.com')
        time.sleep(3)
        driver.find_element_by_name('q').send_keys('youtube trending' + Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
        print ('Initalizing...')
        print ('Finding Video...')
        time.sleep(6)
        search_engine = driver.find_element_by_xpath('//*[@id="video-title"]').click()
        print ('Watching Youtube Video')
        time.sleep(210)

        print ('Finished Youtube Video.')
        print ('----------------------------------')
        print ('Doing some human like google searches...')

        print ('Searching.')
        driver.get('https://www.google.com')
        time.sleep(4)
        search_engine = driver.find_element_by_name('q')
        search_engine.send_keys('twituserjosh twitter' + Keys.RETURN)#if you want to edit the searches
        driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
        time.sleep(10)

        print ('Searching..')
        driver.get('https://www.google.com')
        time.sleep(5)
        search_engine = driver.find_element_by_name('q')
        search_engine.send_keys('theory of everything' + Keys.RETURN)#if you want to edit the searches
        driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
        time.sleep(20)

        print ('Searching...')
        driver.get('https://www.google.com')
        time.sleep(4)
        search_engine = driver.find_element_by_name('q')
        search_engine.send_keys('nellaf' + Keys.RETURN) #if you want to edit the searches
        driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
        time.sleep(15)

        print ('Searching....')
        driver.get('https://www.google.com')
        time.sleep(4)
        search_engine = driver.find_element_by_name('q')
        search_engine.send_keys('adidas' + Keys.RETURN)#if you want to edit the searches
        driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
        time.sleep(10)


        driver.get('https://www.google.com')
        time.sleep(3)
        driver.find_element_by_name('q').send_keys('youtube trending' + Keys.RETURN)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
        print ('Finding Video...')
        time.sleep(6)
        search_engine = driver.find_element_by_xpath('//*[@id="video-title"]').click()
        time.sleep(5)
        print ('Now watching youtube videos infinitely... Stop watching? ')
        end = input ('type "end" to stop: ')


        print ('----------------------------------')
        print (email +' Captcha 1-Click Ready!')
        print ('')



start_time = time.time()
main_function()
print('1-Click generated in ' + " %s seconds " % (time.time() - start_time))
