from dataclasses import replace
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
import time
import pandas as pd
from csv import DictWriter
import csv
import re

driver = webdriver.Chrome(ChromeDriverManager().install())

print("test case started")

#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("https://shopee.sg/")  
#identify the Google search text box and enter the value  
# driver.find_element_by_name("q").send_keys("javatpoint")  
# time.sleep(3)  
# #click on the Google search button  
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
# time.sleep(3)  
# #close the browser 

# closes the popup first
driver.find_element(By.XPATH, "//html").click();

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)

#load
time.sleep(5)


# search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys("sports bra")

# driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

# load
# time.sleep(5)

# driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(Keys.CONTROL,"a")
# driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(Keys.DELETE)

# time.sleep(1)

# driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys("yoga pants")

# driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

# time.sleep(5)

driver.close()  
print("sample test case successfully completed")  

# class Testpythonorgsearch(unittest.TestCase):
#     #initialise
#     def setup(self):
#         self.driver = webdriver.Chrome()
        
#     def test_search(self):
#         driver = self.driver
#         driver.get("https://www.google.com")
#         #ensure that the title has the word inside
#         self.assertIn("Google",driver.title)
#         #find element that you want to get
#         driver.find_element_by_name("q").send_keys("test")
#         driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
#         driver.close()
#         print("test case successful")
        
    