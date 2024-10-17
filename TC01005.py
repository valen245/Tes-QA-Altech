from selenium import webdriver 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException

#open web driver
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
driver.find_element(By.XPATH, '//*[@id="et-boc"]/header/div/div/div/div[3]/div/div/a/span[1]/span').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="post-24"]/div/div/div/div/div/div/div/div/div/form/table/tbody/tr[1]/td[1]/a').click()
time.sleep(6)

#verify element
try:
    driver.find_element(By.XPATH, '//*[@id="post-24"]/div/div/div/div/div/div/div/div/div/div/div')
    print('Pass')
except NoSuchElementException:
    print('Element Not Found')

driver.quit()
