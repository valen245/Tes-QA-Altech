from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException

#open webdriver
driver = webdriver.Chrome() 

#go to link
driver.get('https://demo.tokosatu.com/simple-shop/') 
time.sleep(5) 

#navigate
get_url = driver.current_url
driver.find_element(By.XPATH,'//*[@id="woocommerce-product-search-field-0"]').click()
driver.find_element(By.XPATH,'//*[@id="woocommerce-product-search-field-0"]').send_keys('Google Home')
driver.find_element(By.XPATH,'//*[@id="woocommerce_product_search-2"]/form/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="main-content"]/div[2]/div/div[1]/div[2]/div[2]/div[5]/div/form/button').click()
time.sleep(3)

#verify element
try:
    driver.find_element (By.XPATH,'//*[@id="main-content"]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div')
    print('Pass')
    pass
except NoSuchElementException:
    print('Element Not Found')

driver.quit()


