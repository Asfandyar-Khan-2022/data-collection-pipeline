from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import json
import requests 
import shutil 

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])


class crawler:

   
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.phones_names_list = []
        self.phones_price_list = []
        self.image_url_list = []
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


    def go_into_page_and_out(self):
        in_and_out = self.driver.find_element(By.XPATH, value ='//*[@id="__layout"]/div/div[6]/div[1]/div[2]/div/div/div/div/div[3]/div[1]/div/div[2]/h1/a/span')
        in_and_out.click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
    

    def scroll_to_bottom(self):
        previouse_height = self.driver.execute_script('return document.body.scrollHeight')

        while True:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(3)
            new_height = self.driver.execute_script('return document.body.scrollHeight')

            if new_height == previouse_height:
                break
            previouse_height = new_height

        return True
    

    def gather_image_data(self):
        image_data = self.driver.find_elements(By.CSS_SELECTOR, 'img.t058-product-img')

        for i in image_data:
            dict_image_link = {}
            dict_image_link['Image URL'] = [i.get_attribute('src')]
            self.image_url_list.append(dict_image_link)
    

    def buying_and_selling_price(self):
        new_list = []
        we_sell_price = self.driver.find_elements(By.CSS_SELECTOR, 'div.priceTxt')
        for i in we_sell_price:
            new_list.append(i.text)
        composite_list = [new_list[x:x+3] for x in range(0, len(new_list),3)]

        for i in composite_list:
            dict_phones_price = {}
            dict_phones_price['Price'] = i
            self.phones_price_list.append(dict_phones_price)


    def phone_name_and_condition(self):
        phone_name = self.driver.find_elements(By.CSS_SELECTOR, 'span.ais-Highlight')
        for i in phone_name:
            dict_phones = {'Phone': [], 'Condition': [], 'Price': [], 'Image URL': [], 'Time': []}
            dict_phones['Phone'].append(i.text)
            dict_phones['Condition'].append(i.text[-1])
            self.phones_names_list.append(dict_phones)


    def add_url_price_time_to_dictionary(self):
        for i in range (len(self.phones_names_list)):
            self.phones_names_list[i]['Price'] = self.phones_price_list[i]['Price']
            self.phones_names_list[i]['Image URL'] = self.image_url_list[i]['Image URL']
            now = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            self.phones_names_list[i]['Time'] = now
    

    def download_img(self):    
        for i in range(len(self.image_url_list)):
            image_url = self.image_url_list[i]['Image URL'][0]
            now = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
            filename = f"{now}_{str(i)}.jpg"
            r = requests.get(image_url, stream = True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(filename,'wb') as f:
                    shutil.copyfileobj(r.raw, f)
                    
                print('Image sucessfully Downloaded: ',filename)
            else:
                print('Image Couldn\'t be retreived')
        


if __name__ == "__main__":
    start_crawling = crawler()
    start_crawling.load_and_accept_cookies()
    start_crawling.device_grade()
    start_crawling.go_into_page_and_out()
    if start_crawling.scroll_to_bottom():
        start_crawling.gather_image_data()
        start_crawling.buying_and_selling_price()
        start_crawling.phone_name_and_condition()
        start_crawling.add_url_price_time_to_dictionary()
        start_crawling.download_img()
    start_crawling.driver.quit()

