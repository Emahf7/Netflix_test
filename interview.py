from selenium import webdriver
import time
import sign_up
driver = webdriver.Firefox(executable_path=r"D:\Descargas\geckodriver-v0.30.0-win64\geckodriver")

driver.get("https://www.gmail.com")
time.sleep(6)
driver.find_element_by_css_selector("button.FliLIb > span:nth-child(4)").click()
time.sleep(3)
driver.find_element_by_css_selector("li.G3hhxb:nth-child(2) > span:nth-child(2)").click()

time.sleep(4)


driver.find_element_by_css_selector("#firstName").send_keys(sign_up.name)
time.sleep(4)


driver.find_element_by_css_selector("#lastName").send_keys(sign_up.apellido)
time.sleep(4)

driver.find_element_by_css_selector("#username").send_keys(sign_up.usuario)
time.sleep(4)

driver.find_element_by_css_selector(".VfPpkd-LgbsSe-OWXEXe-k8QpJ > span:nth-child(4)").click()
time.sleep(4)


assert "ingresar" in driver.find_element_by_css_selector("div.SdBahf:nth-child(3) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)").text, "Passed. Expected error"
