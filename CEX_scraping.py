from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class crawler:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)
        self.phones_names_list = []
        self.phones_price_list = []
        self.complete_list = []
    
    def load_and_accept_cookies(self) -> webdriver.Chrome:
        URL = f"https://uk.webuy.com/search?stext=iphone%207%20plus"
        self.driver.get(URL)
        time.sleep(3) 
        try:
            accept_cookies_button = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies_button.click()
            time.sleep(1)
        except:
            pass
    
    def device_grade(self):
        grade_a = self.driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div[6]/div[2]/div[1]/div/div/div[47]/ul/li[3]')
        grade_a.click()
        grade_b = self.driver.find_element(By.XPATH, value='//*[@id="__layout"]/div/div[6]/div[2]/div[1]/div/div/div[47]/ul/li[2]')
        grade_b.click()
    
    def list_all_phones(self):
        dict_phones = {'Phone': [], 'Condition': [], 'Price': []}
        phone_name = self.driver.find_elements(By.CSS_SELECTOR, 'span.ais-Highlight')
        we_sell_price = self.driver.find_elements(By.CSS_SELECTOR, 'div.priceTxt')
        for i in phone_name:
            dict_phones = {'Phone': [], 'Condition': [], 'Price': []}
            dict_phones['Phone'].append(i.text)
            dict_phones['Condition'].append(i.text[-1])
            self.phones_names_list.append(dict_phones)
        for i in we_sell_price:
            dict_phones_price = {'Price': []}
            dict_phones_price['Price'].append(i.text)
            self.phones_price_list.append(dict_phones_price)
        for i in range (len(self.phones_names_list)):
            self.phones_names_list[i]['Price'] = self.phones_price_list[i]['Price']




start_crawling = crawler()
start_crawling.load_and_accept_cookies()
start_crawling.device_grade()
start_crawling.list_all_phones()
print(start_crawling.phones_names_list)
