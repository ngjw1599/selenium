from dataclasses import replace
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
import time
import pandas as pd
from csv import DictWriter
import csv
import re


driver = webdriver.Chrome(ChromeDriverManager().install())

#insert website here
driver.get("https://shopee.sg/-%E2%9C%85LOCAL-Resistance-Bands-Set-Long-Exercise-Bands-Latex-Resistance-Bands-Long-Tension-Fitness-Belt-Strong-Stretch-Band-i.236813629.3138591774?sp_atk=fb08608f-2141-4bbc-944b-26dc689a81b9&xptdk=fb08608f-2141-4bbc-944b-26dc689a81b9")

time.sleep(5)

# putting the data into a csv format
# create headers
column_names = ["Category", "Type", "Title", "Description", "Price", "Sales", "Rating", "Stars", "Reviews"]
#create list 
list_of_info = []

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

driver.maximize_window()


# retrieve all required information
title = driver.find_element(By.CLASS_NAME, "_2rQP1z").text
description = driver.find_element(By.XPATH, "//p[@class='_2jrvqA']").get_attribute('textContent')
price = driver.find_element(By.CLASS_NAME, "_2Shl1j").text
sales = driver.find_element(By.CLASS_NAME, "HmRxgn").text

# webpage doesnt load all elements, thus need to refresh
driver.refresh()
time.sleep(5)
driver.execute_script("window.scrollTo(0,1000)")
time.sleep(5)
driver.execute_script("window.scrollTo(1000,2000)")
time.sleep(8)

#rating
rating = driver.find_element(By.CLASS_NAME, 'product-rating-overview__rating-score').get_attribute("textContent")

# driver refresh
driver.execute_script("window.scrollTo(2000,3500)")
time.sleep(8)

reviews_list = [] 
            

maxbefore = 0
maxafter = 1

beforepagelist = []
afterpagelist = []

while maxbefore != maxafter:
        # get current page max number
        pages = driver.find_elements(By.CLASS_NAME, "shopee-button-no-outline")
        for i in pages:
                beforepagelist.append(i.text)

        # find reviews
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

        # print(beforepagelist)
        # print(afterpagelist)

        maxbefore = max(beforepagelist)
        maxafter = max(afterpagelist)

        # print (maxbefore)
        # print (maxafter)

        beforepagelist.clear()
        afterpagelist.clear()


#input dictionary
dict_data = {
            "Category": 'Fitness Wear',
            "Type": 'Sports Bra', 
            "Title": title, 
            "Description": description, 
            "Price": price,
            "Sales": sales_to_value(sales), 
            "Rating" : rating,
            "Reviews" : reviews_list
            }

            # add into original list for csv
list_of_info.append(dict_data)

#convert into csv, replaces the old one
#rename csv file
with open('resbands4_scraping.csv', 'w', encoding='UTF8', newline='') as convert:
    dw = csv.DictWriter(convert, delimiter=',', fieldnames=column_names)
    dw.writeheader()
    for info in list_of_info:
        dw.writerow(info)

    
#closes the browser once done
driver.close()

#print message once output is done
print("case done successfully")