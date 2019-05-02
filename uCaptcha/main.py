from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
options.headless = False
options.add_argument("--disable-gpu")
options.add_argument("--ignore-certificate-errors-spki-list")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--test-type");
options.add_argument("--disable-gpu");
options.add_argument("--no-first-run");
options.add_argument("--no-default-browser-check");
options.add_argument("--ignore-certificate-errors");

print ("""
    __    _____             _       _
    \ \  /  __ \           | |     | |
 _   \ \ | /  \/ __ _ _ __ | |_ ___| |__   __ _
| | | \ \| |    / _` | '_ \| __/ __| '_ \ / _` |
| |_| |\ \ \__/\ (_| | |_) | || (__| | | | (_| |
 \__,_| \_\____/\__,_| .__/ \__\___|_| |_|\__,_|
                     | |
                     |_|                        """)

email = input('Email: ')
password = input('Password: ')

def main_function():
    driver = webdriver.Chrome(chrome_options=options)
    print ('Logging into Gmail...')
    driver.get('https://www.gmail.com')
    time.sleep(5)
    driver.find_element_by_id('identifierId').send_keys(email)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
    print ('Logged in as: '+ email)
    time.sleep(2)
    print ('Searching for Youtube videos...')
    driver.get('https://www.google.com')
    time.sleep(3)
    driver.find_element_by_name('q').send_keys('1 Hour Long Youtube Videos' + Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="rso"]/div/div/div[1]/div/div/div[1]/a').click()
    print ('Initalizing...')
    print ('Watching Youtube Video')
    time.sleep(250)
    print ('Finished Youtube Video.')
    print ('----------------------------------')
    print ('Randomizing Google searches...')

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
    search_engine.send_keys('fortnite burger' + Keys.RETURN)#if you want to edit the searches
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

    print ('----------------------------------')
    print (email +' Captcha 1-Click Ready!')
    print ('')



start_time = time.time()
main_function()
print('Email prepped in ' + " %s seconds " % (time.time() - start_time))
