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
#driver.get("https://shopee.sg/m/new-user-zone") 

#testing loop pages
driver.get("https://shopee.sg/Women's-summer-latex-seamless-beauty-back-bra-no-steel-ring-ice-silk-to-receive-auxiliary-breast-sports-vest-underwear-bra-set-i.170138673.17569663659?sp_atk=687aad43-cf74-447c-aa23-93fc37671903&xptdk=687aad43-cf74-447c-aa23-93fc37671903")
time.sleep(5)
driver.refresh()
time.sleep(5)
#identify the Google search text box and enter the value  
# driver.find_element_by_name("q").send_keys("javatpoint")  
# time.sleep(3)  
# #click on the Google search button  
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
# time.sleep(3)  
# #close the browser 

# closes the popup first
# driver.find_element(By.XPATH, "//html").click();

# driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)

#load
# time.sleep(5)



product_type = {'Fitness Wear': ["Sports Bra", "Yoga Pants"],
                'Resistance Bands' : ["Fabric Resistance Bands", "Resistance Bands"],
                'Skipping Rope': ["Skipping Rope"]}


maxbefore = 0
maxafter = 1

beforepagelist = []
afterpagelist = []

reviews_list = [] 

while maxbefore != maxafter:
        # get current page max number
        pages = driver.find_elements(By.CLASS_NAME, "shopee-button-no-outline")
        for i in pages:
                beforepagelist.append(i.text)

        driver.find_element(By.CLASS_NAME, "shopee-icon-button--right ").click()

        time.sleep(5)

        reviews_list.append(driver.find_element(By.CLASS_NAME, "product-ratings__list").get_attribute("textContent"))

        time.sleep(3)

        driver.find_element(By.CLASS_NAME, "shopee-icon-button--right ").click()

        time.sleep(3)

        reviews_list.append(driver.find_element(By.CLASS_NAME, "product-ratings__list").get_attribute("textContent"))

        time.sleep(5)

        next_pages = driver.find_elements(By.CLASS_NAME, "shopee-button-no-outline")
        for k in next_pages:
                afterpagelist.append(k.text)

        for i in beforepagelist:
                if i.isdigit() != True:
                        beforepagelist.remove(i)

        for i in afterpagelist:
                if i.isdigit() != True:
                        afterpagelist.remove(i)

        beforepagelist.pop()
        afterpagelist.pop()

        beforepagelist = [eval(i) for i in beforepagelist]
        afterpagelist = [eval(i) for i in afterpagelist]

        print(beforepagelist)
        print(afterpagelist)

        maxbefore = max(beforepagelist)
        maxafter = max(afterpagelist)

        print (maxbefore)
        print (maxafter)

        beforepagelist.clear()
        afterpagelist.clear()


print(reviews_list)




# for main_type in product_type:
#     #print(main_type)
#     for item in product_type[main_type]:
#         #print(item)

#         #find element by class "shopee-searchbar-input", input to search
#         search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(item)

# #search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys("sports bra")

#         driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

# #load
#         time.sleep(5)

#         driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(Keys.CONTROL,"a")
#         driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(Keys.DELETE)

#         # time.sleep(1)

#         # driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys("yoga pants")

#         # driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

#         time.sleep(5)

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
        
    