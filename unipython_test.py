
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\Emanuel\Desktop\geckodriver.exe')
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        time.sleep(3)
        self.assertIn("Python", driver.title)
        time.sleep(3)
        elem = driver.find_element_by_name("q")
        time.sleep(3)
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "No results Found." not in driver.page_source
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
