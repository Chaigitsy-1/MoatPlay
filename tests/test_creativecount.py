'''
Created on 04-Jan-2021

@author: 91986
'''

import unittest
from selenium import webdriver
from pages.Page_searchbar import Page_searchbar
from pages.Page_creative import Page_creative

class Testcreativecount(unittest.TestCase):
    baseurl='https://moat.com/'
    driver=webdriver.Chrome('C:\\Users\\91986\\eclipse-workspace\\moat\\drivers\\chromedriver.exe')
    creatives=["Saturn","Saturday's Market","Krux"]
    creatives_count=[]
    
    def setUp(self):
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        
    def test_TC002(self):
        try:
            pc=Page_creative(self.driver)
            for item in self.creatives:
                cr_count=pc.creative_count_check(item)
                self.creatives_count.append(int(cr_count.replace('creatives','')))
            
            
        except Exception as e:
            print(e)
            raise
        print(self.creatives_count)
        
       
    def tearDown(self):
        self.driver.close()
        #self.driver.close()
if __name__ == '__main__':
    unittest.main()
        
        

        