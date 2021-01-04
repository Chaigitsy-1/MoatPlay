
'''
Created on 04-Jan-2021

@author: 91986
'''
from pages.base_page import BasePage

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from pickle import NONE

class Page_searchbar(BasePage):
    
    searchbar_xpath=(By.XPATH,'//*[@id="adsearch-input"]')
    autofill_id =(By.XPATH,'//*[@id="adsearch-dropdown"]')
    autofill_xpath=(By.XPATH,'//*[@id="adsearch-dropdown"]/div/div[1]/a/div')
    generic_autofill_xpath='//*[@id="adsearch-dropdown"]/div/div[zot]/a/div'
    
    
    
    def __init__(self, driver):
        self.driver = driver
    
    def search_operation(self,brandname):
        print('redirected')
        self.wait_element(*self.searchbar_xpath)
        self.find_element(*self.searchbar_xpath).click()
        self.find_element(*self.searchbar_xpath).send_keys(brandname)
        time.sleep(20)
        
        try:
            self.find_element(*self.autofill_id)
        except Exception as e:
            
            print(e)
            raise 
        try:
            autotext=self.find_element(*self.autofill_xpath).text
            print(autotext)
            if autotext!=None:
                pass
            else:
                raise Exception('search exception') 
        except Exception as e:
            print(e)
            raise      
                