import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from getpass import getpass

driver = webdriver.Chrome()
driver.get('https://maeshima-ami.jp/group/8311')

time.sleep(3)

userID = input('userID: ')
userPasswd = getpass('userPasswd: ')

userIDForm = driver.find_element_by_id('user_login')
userPasswdForm = driver.find_element_by_id('user_password')

userIDForm.send_keys(userID)
userPasswdForm.send_keys(userPasswd)

loginButton = driver.find_element_by_name('commit')
loginButton.click()

time.sleep(4)
imgList = driver.find_elements_by_class_name('img-protect')
print(len(imgList))

for i in imgList:
    source = i.find_element_by_tag_name('data-original')
    print(source)
