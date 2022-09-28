from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
import time
import pandas as pd
import csv


driver = webdriver.Chrome(ChromeDriverManager().install())

#open shopee website
driver.get("https://shopee.sg/")

# closes the popup first
driver.find_element(By.XPATH, "//html").click();

#load
time.sleep(5)

#find element by class "shopee-searchbar-input", input "sports bra" to search
search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys("Sports Bra")

#load
time.sleep(2)

#click on search
driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

#load
time.sleep(5)

#we can for loop later but first manual test each one
# class ="row shopee-search-item-result__items"
#click on the second row, first one

# create table data 
table_result = driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/href]")
print(table_result)

# for row in range(1,12):
#     rows = table_result.find_elements(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]")


#load
# get title
# type; class below
# title: "_2rQP1z" 
# Description: ""._2jrvqA"
# Price: "._2Shl1j"
# Sales: "HmRxgn" : however this is in text format and not number, need to convert
# Ratings/Reviews
    #split into different groups: overall rating: ".product-rating-overview__rating-score"
    # X stars: class="product-rating-overview__filter"; it is in a list format
    # 5 star 
        # comment
    # 4 star
    # 3 star
    # 2 star
    # 1 star
    


#


#closes the browser once done
driver.close()

print("test case done successfully")