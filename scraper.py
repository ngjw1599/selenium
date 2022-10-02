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

# putting the data into a csv format
# create headers
column_names = ["Type", "Title", "Description", "Price", "Sales", "Rating", "Stars", "5 Stars", "4 Stars", "3 Stars", "2 Stars", "1 Star"]
#create list 
list_of_info = []


#click on search
driver.find_element(By.XPATH, "//header/div[2]/div[1]/div[1]/div[1]/button[1]").click()

#load
time.sleep(5)

#we can for loop later but first manual test each one
# class ="row shopee-search-item-result__items"
#click on the second row, first one

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
#item 1-4, div 6-9
for div_item in range(6,10):
    item=str(div_item)
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div/div[2]/div/div[2]/div[" + item +"]/a/div/div").click()
    driver.refresh()
    time.sleep(5)
    title = driver.find_element(By.CLASS_NAME, "_2rQP1z").text
    #get the text description that contains the word "Bra"
    #testing
    description = driver.find_element(By.XPATH, "//p[@class='_2jrvqA']").get_attribute('textContent')
    #description = driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/div[2]/div/p" ).get_attribute("textContent")
    price = driver.find_element(By.CLASS_NAME, "_2Shl1j").text
    sales = driver.find_element(By.CLASS_NAME, "HmRxgn").text

    driver.refresh()
    time.sleep(5)
    #rating
    rating = driver.find_element(By.CLASS_NAME, 'product-rating-overview__rating-score').get_attribute("textContent")

    #get number of stars
    #stars
    stars = driver.find_elements(By.XPATH, "//div[@class='product-rating-overview__filter']")
    liststars = []
    for i in range(len(stars)):
        liststars.append(stars[i].text)
    # five_stars = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[2]').text
    # #five = re.findall(r"\[((A-Za-z0-9_)+)\]", five_stars)
    
    # four_stars = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[3]').text
    # #four = re.findall(r'\(.*?\')', four_stars)

    # three_stars = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[4]').text
    # #three = re.findall(r'\(.*?\')', three_stars)

    # two_stars = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[5]').text
    # #two = re.findall(r'\(.*?\')', two_stars)

    # one_star = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[6]').text
    # #one = re.findall(r'\(.*?\')', one_star)


    #input dictionary
    dict_data = {"Type": "Sports Bra", 
                "Title": title, 
                "Description": description, 
                "Price": price,
                "Sales": sales_to_value(sales), 
                "Rating" : rating,
                "Stars" : liststars
                # "5 Stars": five_stars, 
                # "4 Stars": four_stars,
                # "3 Stars": three_stars,
                # "2 Stars": two_stars,
                # "1 Star": one_star
                }

    # add into original list for csv
    list_of_info.append(dict_data)

    #return to the previous page
    driver.back()

#item 1
#driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[6]/a[1]/div[1]/div[1]").click()


#time.sleep(5)

# title = driver.find_element(By.CLASS_NAME, "_2rQP1z").text
# #get the text description that contains the word "Bra"
# description = driver.find_element(By.XPATH, "//p[contains(text(),'Bra')]" or "//p[contains(text(),'bra')]" ).get_attribute("textContent")
# price = driver.find_element(By.CLASS_NAME, "_2Shl1j").text
# sales = driver.find_element(By.CLASS_NAME, "HmRxgn").text



#input dictionary
#dict_data = {"Type": "Sports Bra", "Title": title, "Description": description, "Price": sales_to_value(sales)}

#test post values below
# for value in dict_data.values():
#     print(value)

#append dictionary into list
#list_of_info.append(dict_data)

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