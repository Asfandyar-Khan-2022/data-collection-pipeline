from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
driver.get(URL)
time.sleep(2) # Wait a couple of seconds, so the website doesn't suspect you are a bot

def load_and_accept_cookies() -> webdriver.Chrome:
    '''
    Open Zoopla and accept the cookies
    
    Returns
    -------
    driver: webdriver.Chrome
        This driver is already in the Zoopla webpage
    '''
    URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
    driver.get(URL)
    time.sleep(3) 
    try:
        driver.switch_to_frame('gdpr-consent-notice') # This is the id of the frame
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        accept_cookies_button.click()
        time.sleep(1)
    except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
        driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        accept_cookies_button.click()
        time.sleep(1)

    except:
        pass

    return driver 

time.sleep(2)
load_and_accept_cookies()

house_property = driver.find_element(by=By.XPATH, value='//*[@id="listing_62867916"]')
a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
link = a_tag.get_attribute('href')

driver.get(link)

dict_properties = {'Price': [], 'Address': [], 'Bedrooms': [], 'Description': []}
price = driver.find_element(by=By.XPATH, value='//p[@data-testid="price"]').text
dict_properties['Price'].append(price)
address = driver.find_element(by=By.XPATH, value='//address[@data-testid="address-label"]').text
dict_properties['Address'].append(address)
bedrooms = driver.find_element(by=By.XPATH, value='//div[@class="c-PJLV c-PJLV-iiNveLf-css"]').text
dict_properties['Bedrooms'].append(bedrooms)
div_tag = driver.find_element(by=By.XPATH, value='//div[@data-testid="truncated_text_container"]')
span_tag = div_tag.find_element(by=By.XPATH, value='.//span')
description = span_tag.text
dict_properties['Description'] = description
print(dict_properties)

driver.quit()

