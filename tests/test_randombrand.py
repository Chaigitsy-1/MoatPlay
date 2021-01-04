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

class Testrandombrand(unittest.TestCase):
    baseurl='https://moat.com/advertiser/saturn'
    driver=webdriver.Chrome('C:\\Users\\91986\\eclipse-workspace\\moat\\drivers\\chromedriver.exe')
    randomlist=[]
    randomlist1=[]
    
    def setUp(self):
        print(self.baseurl)
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        
    def test_TC003(self):
        try:
            
            print('003')
            pr=Page_randombrand(self.driver)
            '''
            for i in range(0,3):
                self.randomlist.append(pr.randombrand_name())
                time.sleep(2)
            print(self.randomlist)
           '''
            randomlist=pr.randomchecker()
            randomlist1=pr.randomchecker()
            print(randomlist)
            print(randomlist1)
            if randomlist!=randomlist1:
                raise
        except Exception as e:
            print(e)
            raise
        
      
          
    def tearDown(self):
        self.driver.close()
        #self.driver.close()
if __name__ == '__main__':
    unittest.main()
        
        

        