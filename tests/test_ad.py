'''
Created on 04-Jan-2021

@author: 91986
'''

import time
import unittest
from selenium import webdriver
from pages.Page_searchbar import Page_searchbar
from pages.Page_creative import Page_creative
from pages.Page_randombrand import Page_randombrand
from pages.Page_ad import Page_ad

class Testad(unittest.TestCase):
    baseurl='https://moat.com/advertiser/saturn'
    driver=webdriver.Chrome('C:\\Users\\91986\\eclipse-workspace\\moat\\drivers\\chromedriver.exe')
    copiedlink=''
    
    def setUp(self):
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
 
 
    def test_TC004(self):
        try:
            pa=Page_ad(self.driver)
            
            pa.page_ad()
            
        except Exception as e:
            print(e)
            raise
       
    def tearDown(self):
        self.driver.close()
        #self.driver.close()

               