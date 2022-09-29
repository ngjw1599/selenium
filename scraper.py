from dataclasses import replace
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  
import time
import pandas as pd
from csv import DictWriter
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
time.sleep(5)

#click on search
driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

#load
time.sleep(5)

#we can for loop later but first manual test each one
# class ="row shopee-search-item-result__items"
#click on the second row, first one

# create table data 


#item 1
driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]/div[6]/a[1]/div[1]/div[1]").click()

time.sleep(5)

title = driver.find_element(By.CLASS_NAME, "_2rQP1z").text
#get the text description that contains the word "Bra"
description = driver.find_element(By.XPATH, "//p[contains(text(),'Bra')]" or "//p[contains(text(),'bra')]" ).get_attribute("textContent")
price = driver.find_element(By.CLASS_NAME, "_2Shl1j").text
sales = driver.find_element(By.CLASS_NAME, "HmRxgn").text

#convert sales in text to number
def sales_to_value(sales):
    if type(sales) == float or type(sales) == int:
        return sales
    if 'k' in sales:
        if len(sales)>1:
            sales = float(sales.replace("k", '') )* 1000
            return sales
    else:
        return float(sales)
    
    
# putting the data into a csv format
# create headers
column_names = ["Type", "Title", "Description", "Price", "Sales"]
#create list 
list_of_info = []

#input dictionary
dict_data = {"Type": "Sports Bra", "Title": title, "Description": description, "Price": sales_to_value(sales)}

#test post values below
# for value in dict_data.values():
#     print(value)

#append dictionary into list
list_of_info.append(dict_data)

#convert into csv, replaces the old one
with open('scraping.csv', 'w', encoding='UTF8', newline='') as convert:
    dw = csv.DictWriter(convert, delimiter=',', fieldnames=column_names)
    dw.writeheader()
    for info in list_of_info:
        dw.writerow(info)

#there has to be another way to deal with this lol, like a looping through but i am unable to get the link data using XPATH :(

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
    
#closes the browser once done
driver.close()

#print message once output is done
print("test case done successfully")