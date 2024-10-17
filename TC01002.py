from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import selenium.webdriver.common.keys
from selenium.common.exceptions import NoSuchElementException

#open webdriver
driver = webdriver.Chrome() 
 
#go too link
driver.get('https://demo.tokosatu.com/simple-shop/') 
time.sleep(5) 

#navigate
driver.find_element(By.XPATH,'//*[@id="woocommerce-product-search-field-0"]').click()
driver.find_element(By.XPATH,'//*[@id="woocommerce-product-search-field-0"]').send_keys('Google Home')
driver.find_element(By.XPATH,'//*[@id="woocommerce_product_search-2"]/form/button').click()
time.sleep(5)

#verify element
if driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/div/div[1]/div[2]'):
    get_text = driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/h1').text
    assert get_text == 'Google Home'
    print('Match')
else:
    print('Element not found')
driver.quit() 
