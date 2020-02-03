import requests
from selenium import webdriver
import time
from getpass import getpass
import os

driver = webdriver.Chrome()
driver.get('https://maeshima-ami.jp/group/8311')

#time.sleep(3)

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

#保存用ディレクトリ作成, 存在していた場合はエラー
#os.mkdir('amitaImgDir')

for listNum, img in enumerate(imgList):
    imgURL = img.get_attribute('data-original')
    response = requests.get(imgURL)

    with open('amitaImgDir/amita' + str(listNum) + '.png', 'wb') as imgBin:
        imgBin.write(response.content)
