import unittest
from selenium import webdriver
import time
from selenium
class suite(unittest.Testcase):
    def setUp(self):
        self.Fdriver = webdriver.Firefox(executable_path=r'C:\Users\Emanuel\Desktop\geckodriver.exe')


    def test_busqueda(self):
        self.Fdriver.get("http://www.google.com/")
        self.busqueda = self.Fdriver.find_element_by_name("q")
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(3)

    def  test_outlook(self):
        self.Fdriver = webdriver.Firefox(executable_path=r'C:\Users\Emanuel\Desktop\geckodriver.exe')
        self.Fdriver.get("http://www.outlook.com/")
        time.sleep(3)


    def test_link_text(self):
        driver = self.Fdriver
        self.Fdriver.get("https://www.3schools.com/")
        time.sleep(3)
        link = self.Fdriver.find_element_by_link_text("Learn Python")
        link.click()
        time.sleep(3)


    def tearDown(self):
        self.Fdriver.quit()

if __name__ == '__main__':
    unittest.main()
