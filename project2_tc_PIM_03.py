#Header validation on admin page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait






# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec




class Form:

   
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)


   def boot(self):
       self.driver.get(self.url)
       self.driver.maximize_window()
       self.wait.until(ec.url_to_be(self.url))
       
   def quit(self):
       self.driver.quit()

       
 #Menu option admin is displaying in Admin page  
   def check_Admin_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Admin option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option PIM is displaying in Admin page  
   def check_PIM_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("PIM option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Leave is displaying in Admin page  
   def check_Leave_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Leave option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Time is displaying in Admin page  
   def check_Time_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Time option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Recriutment is displaying in Admin page  
   def check_Recriutment_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Recriutment option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option MyInfo is displaying in Admin page  
   def check_MyInfo_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("MyInfo option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Performance is displaying in Admin page  
   def check_MyInfo_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Performance  option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Dashboard is displaying in Admin page  
   def check_Dashboard_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Dashboard  option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Directory is displaying in Admin page  
   def check_Directory_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Directory  option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Maintence is displaying in Admin page
   def check_Maintence_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Maintence  option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Claim is displaying in Admin page
   def check_Claim_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Claim  option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Menu option Buzz is displaying in Admin page
   def check_Buzz_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Buzz  option  is displaying in Admin page")
        except NoSuchElementException:
            return False
        return True
        
              
                
   def login(self):
       self.boot()
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"))).send_keys("Admin")
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"))).send_keys("admin123")
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))).click()
       sleep(10)
       
       
obj = Form("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.login()
obj.check_Admin_by_xpath()
obj.check_PIM_by_xpath()
obj.check_Leave_by_xpath()
obj.check_Time_by_xpath()
obj.check_Recriutment_by_xpath()
obj.check_MyInfo_by_xpath()
obj.check_MyInfo_by_xpath()
obj.check_Dashboard_by_xpath()
obj.check_Directory_by_xpath()
obj.check_Maintence_by_xpath()
obj.check_Claim_by_xpath()
obj.check_Buzz_by_xpath()
obj.quit()