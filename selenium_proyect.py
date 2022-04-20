import csv
import pytest
import conf
import pathlib
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome("/Users/alexissoko/Desktop/chromedriver")

# driver.get("https://www.gmail.com/")
driver.get("https://www.netflix.com/")

def test_title():
    '''
    doc_strings explicative
    '''
    assert 'Netflix' in driver.title

def test_wrong_login():
    '''
    another test comment
    doc_strings explicative
    '''
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@class ="authLinks redButton"]').click()

    loginBox = driver.find_element_by_id('id_userLoginId')
    loginBox.send_keys(conf.user)

    password = driver.find_element_by_id('id_password')
    password.send_keys(conf.password)

    driver.find_element_by_xpath('//*[@class ="btn login-button btn-submit btn-small"]').click()
    login_error_message = driver.find_element_by_xpath('//*[@class ="inputError"]')

    assert "Please" in login_error_message.text

def test_happy_login():
    '''
    another test comment
    doc_strings explicative
    '''
    driver.implicitly_wait(3)
    # driver.find_element_by_xpath('//*[@class ="authLinks redButton"]').click()

    loginBox = driver.find_element_by_id('id_userLoginId')
    loginBox.clear()
    loginBox.send_keys(conf.user_2)

    password = driver.find_element_by_id('id_password')
    password.clear()
    password.send_keys(conf.password_2)

    driver.find_element_by_xpath('//*[@class ="btn login-button btn-submit btn-small"]').click()
    # login_error_message = driver.find_element_by_xpath('//*[@class ="inputError"]')
    label = driver.find_element_by_xpath('//*[@class ="profile-gate-label"]')
    print("label ", label)
    assert "viendo" in label.text
    driver.implicitly_wait(3)

    driver.close()
