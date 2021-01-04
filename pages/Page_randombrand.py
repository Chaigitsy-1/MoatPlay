'''
Created on 04-Jan-2021

@author: 91986
'''
    
from pages.base_page import BasePage

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pages.Page_searchbar import Page_searchbar

class Page_randombrand(Page_searchbar):
    randombrand_xpath=(By.XPATH,'//*[@id="main-nav"]/div[1]/div[1]/a[2]')
    creative_title_xpath=(By.XPATH,'//*[@id="er-app"]/div/div[2]/div/div[1]/span[1]')
    randlist=[]
    def __init__(self, driver):
        self.driver = driver
        
    def randombrand_name(self):
        self.wait_element(*self.randombrand_xpath)
        self.find_element(*self.randombrand_xpath).click()
        print(self.find_element(*self.creative_title_xpath).text)
        return self.find_element(*self.creative_title_xpath).text
    
    def randomchecker(self):
        randlist=[]
        
        print('003')
            
        for i in range(0,3):
            self.randlist.append(self.randombrand_name())
            time.sleep(2)
            print(self.randlist)
           
      
              
        
