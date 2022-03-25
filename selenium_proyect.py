
import pytest
import conf

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Firefox(executable_path=r'C:\Users\Emanuel\Desktop\geckodriver.exe')

# driver.get("https://www.gmail.com/")
driver.get("https://www.netflix.com/")

def test_title():
    '''
    doc_strings explicative
    '''
    assert 'Netflix' in driver.title

def test_wrong_login():
    '''
    test comment
    doc_strings explicative
    '''
    driver.implicitly_wait(15)

    driver.find_element_by_xpath('//*[@class ="authLinks redButton"]').click()
    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(conf.user)

    loginBox = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(conf.user)

    assert driver.title == "success"
