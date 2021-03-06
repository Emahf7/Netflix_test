import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
  driver = webdriver.Firefox(executable_path=r'C:\Users\Emanuel\Desktop\geckodriver.exe')
  driver.implicitly_wait(10)
  yield driver
  driver.quit()
def test_basic_duckduckgo_search(browser):
  URL = 'https://www.duckduckgo.com'
  PHRASE = 'panda'

  browser.get(URL)

  search_input = browser.find_element_by_id('search_form_input_homepage')
  search_input.send_keys(PHRASE + Keys.RETURN)

  link_divs = browser.find_elements_by_css_selector('#links > div')
  assert len(link_divs) > 0

  xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
  results = browser.find_elements_by_xpath(xpath)
  assert len(results) > 0

  search_input = browser.find_element_by_id('search_form_input')
  assert search_input.get_attribute('value') == PHRASE
