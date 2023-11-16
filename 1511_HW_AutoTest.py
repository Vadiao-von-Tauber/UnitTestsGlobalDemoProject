import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class RadioRecordGrandTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.pageSetUp()
        self.credsSetUp()

    def pageSetUp(self) -> None:
        self.page_url = "https://www.radiorecord.ru/"
        self.driver.get(self.page_url)

    def credsSetUp(self) -> None:
        self.eml = "doomersnotdead@gmail.com"
        self.psw = "sabbra_kadabbrra_1967_and_forever"

    def tearDown(self) -> None:
        self.driver.quit()

    def test_00_open_main_page(self) -> None:
        time.sleep(5)

    def test_01_sign_in(self) -> None:
        self.select_sign_in = self.\
            driver.find_element\
            (By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div.xOLoLm09Pwv2jvYf\+ZN4vA\=\= > div > div > button.kewvhzyseTV54oRB2IkmLg\=\= > div._5hMllja8P-ZZrYS8Y2Yc-w\=\=")
        self.select_sign_in.click()
 # By.ID здесь говорит "пока!", на странице много элементов
 # с одинаковыми названиями, поэтому пришлось прописывать здесь и далее через By.CSS_SELECTOR."""""

        self.input_login = self.driver.\
            find_element\
            (By.CSS_SELECTOR,\
                         "#root > div.zwbJrjp5Dz-\+Uj4OBVCj\+g\=\=.BFlcmVBqzs6aPCnnoSwOTQ\=\= > div.vUtif97fh\+EvmFwSY3JPoA\=\= > div:nth-child(1) > div:nth-child(4) > div > input")
        self.input_login.send_keys(self.eml)
        time.sleep(5)
        self.input_psw = self.\
            driver.find_element\
            (By.CSS_SELECTOR,\
                                "#root > div.zwbJrjp5Dz-\+Uj4OBVCj\+g\=\=.BFlcmVBqzs6aPCnnoSwOTQ\=\= > div.vUtif97fh\+EvmFwSY3JPoA\=\= > div:nth-child(1) > div:nth-child(5) > div > input")
        self.input_psw.send_keys(self.psw)
        time.sleep(5)

        self.submit_button_click = self.\
            driver.find_element\
            (By.CSS_SELECTOR,\
                                "#root > div.zwbJrjp5Dz-\+Uj4OBVCj\+g\=\=.BFlcmVBqzs6aPCnnoSwOTQ\=\= > div.vUtif97fh\+EvmFwSY3JPoA\=\= > div:nth-child(1) > button")
        self.submit_button_click.click()
        time.sleep(10)

    def test_02_select_the_synthwave_station_and_run(self) -> None:
        self.run_synthwave_station = self.\
            driver.find_element\
            (By.CSS_SELECTOR,"#root > div > div:nth-child(2) > div.t713H-v8smf6d-AvVWk7oA\=\= > div.gvyT5UV\+5lBoe6E6F6IDuQ\=\=.qg73kVb8cbzNvxFufgIVxg\=\=.PcxRmRYr98sFKNWFgneriA\=\= > div > div.LRsUH1RV1GIy1J0HAHhqxw\=\= > ul > li:nth-child(81) > button > div")
        self.run_synthwave_station.click()
        time.sleep(20) # В виду сильной перегруженности моей машины поставил 20 секунд.

    def test_03_look_the_event_back_to_future(self) -> None:
        self.click_to_event = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div.t713H-v8smf6d-AvVWk7oA\=\= > div.gvyT5UV\+5lBoe6E6F6IDuQ\=\=.qg73kVb8cbzNvxFufgIVxg\=\=.YKnYl6KqMKahhiTPpGeQaA\=\= > nav > ul > li:nth-child(3) > a")
        self.click_to_event.click()
        time.sleep(10)

        self.open_the_event = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div.t713H-v8smf6d-AvVWk7oA\=\= > div.gvyT5UV\+5lBoe6E6F6IDuQ\=\=.qg73kVb8cbzNvxFufgIVxg\=\=.ZsvGzTiMKzMjUCWGdAUwKg\=\= > div > ul > li > div > div.v62QXO8HDAqdkNmNPS1Vqg\=\= > a")
        self.open_the_event.click()
        time.sleep(5)

    def test_04_search_and_play_60s_dance_station(self) -> None:
        self.search_field_button = self.driver.find_element(By.CSS_SELECTOR, "#root > div > div:nth-child(2) > div.xOLoLm09Pwv2jvYf\+ZN4vA\=\= > div > div > div._7ZmC9p4jZBfVHPcBmbzCJA\=\=._83aCOalqeUw-TKY1MQtfEA\=\=._4MpX5FAVIkHOnT\+BSIQ\+Bg\=\= > div > svg")
        self.search_field_button.click()
        time.sleep(7)

        self.search_field = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div:nth-child(2) > div.xOLoLm09Pwv2jvYf\+ZN4vA\=\= > div > div > form > div > div > input")
        self.search_field.send_keys("60's Dance")
        time.sleep(10)

        self.select_60s_dance_station_in_list = self.driver.find_element(By.CSS_SELECTOR,"#root > div > div:nth-child(2) > div.xOLoLm09Pwv2jvYf\+ZN4vA\=\= > div > div > form > div.g9-AN8r7U2HlI\+l-MV8FrQ\=\= > div > ul > li > a")
        self.select_60s_dance_station_in_list.click()
        time.sleep(10)

        self.let_go_old_rocknroll = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[3]/button[2]/div")
        self.let_go_old_rocknroll.click()
        time.sleep(60)
      # Let go rock'n'roll

if __name__ == '__main__':
   unittest.main()