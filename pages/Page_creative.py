'''
Created on 04-Jan-2021

@author: 91986
'''

from pages.Page_searchbar import Page_searchbar

    
from pages.base_page import BasePage

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class Page_creative(Page_searchbar):
    
    creative_title_xpath=(By.XPATH,'//*[@id="er-app"]/div/div[2]/div/div[1]/span[1]')
    creative_count_xpath=(By.XPATH,'//*[@id="er-app"]/div/div[2]/div/div[2]/span')
    
    def __init__(self, driver):
        self.driver = driver
    
    def creative_count_check(self,brandname):
        print('redirected to Page_creative')
        self.search_operation(brandname)
        self.brandfinder=''
        self.count=1
        self.stor=''
        while(self.brandfinder!=brandname):
            
            self.genfill=self.generic_autofill_xpath.replace('zot',str(self.count))
            print(self.genfill)
            self.genfill_xpath=(By.XPATH,self.genfill)
            self.brandfinder=self.find_element(*self.genfill_xpath).text
            print(self.brandfinder)
            self.count=self.count+1
        self.wait_element(*self.genfill_xpath) 
        self.find_element(*self.genfill_xpath).click()
        self.wait_element(*self.creative_title_xpath)
        print(self.find_element(*self.creative_title_xpath).text)
        self.stor=self.find_element(*self.creative_count_xpath).text
        time.sleep(5)
        self.driver.execute_script("window.history.go(-1)")
        return self.stor
    
    
    
            
            
            
        
            
            
        
        

        
         
        
           
                

