from selenium import webdriver 
import time 

#open driver
driver = webdriver.Chrome() 
 
#go to web
driver.get('https://demo.tokosatu.com/simple-shop/') 
time.sleep(5) 

#verify url
get_url = driver.current_url
if get_url == ('https://demo.tokosatu.com/simple-shop/'):
	print('Url Sama')
else:
	print('Url tidak sama')
driver.quit() 

