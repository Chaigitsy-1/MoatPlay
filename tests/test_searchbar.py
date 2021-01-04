'''
Created on 04-Jan-2021

@author: 91986
'''

import unittest
from selenium import webdriver
from pages.Page_searchbar import Page_searchbar

class Testsearchbar(unittest.TestCase):
    baseurl='https://moat.com/'
    driver=webdriver.Chrome('C:\\Users\\91986\\eclipse-workspace\\moat\\drivers\\chromedriver.exe')
    
    
    
    def setUp(self):
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        
    def test_TC001(self):
        ps=Page_searchbar(self.driver)
        ps.search_operation('zo')
        
        
       
    def tearDown(self):
        self.driver.close()
        #self.driver.close()
if __name__ == '__main__':
    unittest.main()
        
        

        