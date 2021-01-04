'''
Created on 04-Jan-2021

@author: 91986
'''

from pages.Page_searchbar import Page_searchbar

    
from pages.base_page import BasePage

from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class Page_ad(BasePage):
    shareurl=''
    ad_xpath=(By.XPATH,'//*[@id="er-app"]/div/div[4]/div[1]/div[2]/div[1]/div/img')
    share_ad_xpath=(By.XPATH, '//*[@id="er-app"]/div/div[4]/div[1]/div[1]/div[4]/div/div/a')
    copy_xpath=(By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[1]')
    copy_button_xpath=(By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[2]/button')
   # /html/body/div[3]/div/div/div/div[2]/div[1]
    
    def __init__(self, driver):
        self.driver = driver
    
    
    
    
    
    def page_ad(self):
        
        self.wait_element(*self.ad_xpath)
        self.find_element(*self.ad_xpath).click()
        self.wait_element(*self.share_ad_xpath)
        self.find_element(*self.share_ad_xpath).click()
        self.wait_element(*self.copy_button_xpath)
        self.find_element(*self.copy_button_xpath).click()

        
    