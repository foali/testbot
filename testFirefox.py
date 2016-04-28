from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
#<class 'selenium.webdriver.firefox.webdriver.WebDriver'>

def login(Id, browser):
	browser.get('http://tenhou.net/3/beta.html')
	try: 
		element = WebDriverWait(browser, 5).until(
			EC.visibility_of_element_located((By.NAME,"ok"))
		)
	
		Boxlogin = browser.find_element_by_name("uname")
		Boxlogin.clear()
		Boxlogin.send_keys(Id)
		ConnectButton = browser.find_element_by_name("ok")
		ConnectButton.click()
		#Connect

		element = WebDriverWait(browser, 5).until(
			EC.visibility_of_element_located((By.NAME,"paneNext"))
		)
		Next = browser.find_element_by_name("paneNext")
		Next.click()

		Next.click()

		browser.find_element_by_xpath("//select[@id='rule0']/option[@value='9']").click()
		Join = browser.find_element_by_id("join0")
		Join.click()
		#Join lobby 4 player open tanyaho aka dora
		value = 0
	except:
		print("lol")
		value = 1
	finally:
		return value 

if __name__ == '__main__':
	Id =  "ID5B6E00E7-dWEDAa57"
	browser = webdriver.Firefox()
	type(browser)
	value = login(Id, browser)
	browser.find_element_by_xpath("//select[@id='rule1']/option[@value='65']").click()
	time.sleep(5)
	browser.quit() #pour l'instant 
