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

#open shopee website
driver.get("https://shopee.sg/m/new-user-zone")

# closes the popup first
driver.find_element(By.XPATH, "//html").click();


#load
time.sleep(5)

product_type = {'Fitness Wear': ["Sports Bra", "Yoga Pants"],
                'Resistance Bands' : ["Fabric Resistance Bands", "Resistance Bands"],
                'Skipping Rope': ["Skipping Rope"]}


# putting the data into a csv format
# create headers
column_names = ["Category", "Type", "Title", "Description", "Price", "Sales", "Rating", "Stars", "Reviews"]
#create list 
list_of_info = []

for main_type in product_type:
    #print(main_type)
    for item in product_type[main_type]:
        #print(item)

        #find element by class "shopee-searchbar-input", input to search
        search_input = driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(item)

        #load
        time.sleep(5)

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
            num_item=str(div_item)
            time.sleep(5)
            driver.find_element(By.XPATH, "//*[@id='main']/div/div[2]/div[1]/div/div[2]/div/div[2]/div[" + num_item +"]/a/div/div").click()

            # webpage doesnt load all elements, thus need to refresh
            driver.refresh()
            time.sleep(5)

            # retrieve all required information
            title = driver.find_element(By.CLASS_NAME, "_2rQP1z").text
            description = driver.find_element(By.XPATH, "//p[@class='_2jrvqA']").get_attribute('textContent')
            price = driver.find_element(By.CLASS_NAME, "_2Shl1j").text
            sales = driver.find_element(By.CLASS_NAME, "HmRxgn").text

            # webpage doesnt load all elements, thus need to refresh
            driver.refresh()
            time.sleep(5)
            driver.refresh()
            time.sleep(5)
            driver.refresh()
            time.sleep(2)

            #rating
            rating = driver.find_element(By.CLASS_NAME, 'product-rating-overview__rating-score').get_attribute("textContent")

            #next page:
            next_page = driver.find_element(By.CLASS_NAME, "shopee-icon-button shopee-icon-button--right") 
            #xpath: //*[@id="main"]/div/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div[2]/button[11]

            reviews_list = [] 
            
            # reviews = driver.find_element(By.CLASS_NAME, "product-ratings__list").get_attribute("textContent")

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
                        "Category": main_type,
                        "Type": item, 
                        "Title": title, 
                        "Description": description, 
                        "Price": price,
                        "Sales": sales_to_value(sales), 
                        "Rating" : rating,
                        "Reviews" : reviews
                        }


            #get number of stars
            #stars

            # stars = driver.find_elements(By.XPATH, "//div[@class='product-rating-overview__filter']")
            # dict_stars = {}
            # for i in range(len(stars)):
            #     for z in range(1,6):
            #         #print(stars[i].text)
            #         dict_stars["{0} Stars".format(z)] = re.findall('\(.*?\)', (stars[i].text)[0])
            
            #get all reviews
            # need to loop through all pages, currently only able to loop through one post

            # add into original list for csv
            list_of_info.append(dict_data)

            #return to the previous page
            driver.back()
        # clear input and go to next item
        driver.refresh()
        driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(Keys.CONTROL,"a")
        driver.find_element(By.CLASS_NAME, "shopee-searchbar-input__input").send_keys(Keys.DELETE)

#convert into csv, replaces the old one
with open('scraping.csv', 'w', encoding='UTF8', newline='') as convert:
    dw = csv.DictWriter(convert, delimiter=',', fieldnames=column_names)
    dw.writeheader()
    for info in list_of_info:
        dw.writerow(info)

    
#closes the browser once done
driver.close()

#print message once output is done
print("test case done successfully")