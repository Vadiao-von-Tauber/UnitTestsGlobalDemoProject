import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class GoogleMailBoxTest(unittest.TestCase):
   def setUp(self) -> None:
      self.driver = webdriver.Chrome()
      self.pageSetUp()
      self.logpassSetUp()
      self.webDriverSetUp()

   def pageSetUp(self) -> None:
      self.page_url = 'https://www.google.com/intl/ru/gmail/about/'
      self.driver.get(self.page_url)

   def logpassSetUp(self) -> None:
      self.eml = "doomersnotdead@gmail.com"
      self.psw = "sabbra_kadabbrra_1967_and_forever"

   def webDriverSetUp(self) -> None:
      self.driver.maximize_window()

   def tearDown(self) -> None:
      self.driver.quit()

   def test_00_open_gmail_main_page(self) -> None:
      time.sleep(3)

   def test_01_log_pass_actions(self) -> None:
      self.enter_mailbox_button_click = self.driver.find_element(By.CSS_SELECTOR, "body > header > div > div > div > a.button.button--medium.button--mobile-before-hero-only")
      self.enter_mailbox_button_click.click()
      time.sleep(3)

      self.input_email = self.driver.find_element(By.CSS_SELECTOR, "#identifierId")
      self.input_email.send_keys(self.eml)
      time.sleep(1)

      self.submit_email = self.driver.find_element(By.ID, "identifierNext")
      self.submit_email.click()
      time.sleep(3)

      self.input_psw = self.driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
      self.input_psw.send_keys(self.psw)
      time.sleep(1)

      self.submit_psw = self.driver.find_element(By.ID, "passwordNext")
      self.submit_psw.click()
      time.sleep(3)

   def test_02_open_letter_field_and_write(self) -> None:
      self.enter_mailbox_button_click = self.driver.find_element(By.CSS_SELECTOR, "body > header > div > div > div > a.button.button--medium.button--mobile-before-hero-only")
      self.enter_mailbox_button_click.click()
      time.sleep(1)

      self.input_email = self.driver.find_element(By.CSS_SELECTOR, "#identifierId")
      self.input_email.send_keys(self.eml)
      time.sleep(5)

      self.submit_email = self.driver.find_element(By.ID, "identifierNext")
      self.submit_email.click()
      time.sleep(3)

      self.input_psw = self.driver.find_element(By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
      self.input_psw.send_keys(self.psw)
      time.sleep(3)

      self.submit_psw = self.driver.find_element(By.ID, "passwordNext")
      self.submit_psw.click()
      time.sleep(5)


if __name__ == '__main__':
   unittest.main()
