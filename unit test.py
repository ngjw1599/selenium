#organising the test case
import unittest

#importing the web driver that we will be using ie:chrome to conduct webscraping
from selenium import webdriver
#keys class on the keyboard
from selenium.webdriver.common.keys import Keys
#by class used to locate elements within the document
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

print("test case started")

driver = webdriver.Chrome()  
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
        
    