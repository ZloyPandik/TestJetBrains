import unittest
from selenium import webdriver
import time

class Tittle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe")
    def test_1tittle(self):
        driver = self.driver
        driver.get("https://jetbrains.com/")
        self.assertIn("JetBrains: Essential tools for software developers and teams", driver.title)
        elem = driver.find_element_by_tag_name("h1")
        self.assertNotIn("No results found.", driver.page_source)
    def test_2inputfield(self):
        driver = self.driver
        driver.get("https://account.jetbrains.com/login")
        username = driver.find_element_by_id("username")
        username.clear()
        username.send_keys("qwerty@yandex.com")
        Password = 1234
        pass_input = driver.find_element_by_name("password")
        pass_input.clear()
        pass_input.send_keys(Password)
        enter_login = driver.find_element_by_class_name("btn").click()
    def test_3window(self):
        driver = self.driver
        driver.get("https://jetbrains.com/")
        time.sleep()
        elem = driver.find_element_by_class_name("jetbrains-cookies-banner__body")
    def tearDown(self):
        self.driver.close()
if __name__ == "__main__":
    unittest.main()