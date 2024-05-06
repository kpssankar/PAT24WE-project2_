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
       
 #Validate title of the page as OrangeHRM      
   def check_OrangeHRM_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Title of the page avilable as OrangeHRM")
        except NoSuchElementException:
            return False
        return True
        
   #Validate title of the page as UserManagement      
   def check_UserManagement_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("UserManagement option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
   #Validate title of the page as Job      
   def check_Job_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Job option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
        
   #Validate title of the page as Organization     
   def check_Organization_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Organization option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
   #Validate title of the page as Qualifications     
   def check_Qualifications_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Qualifications option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
   #Validate title of the page as Nationalities     
   def check_Nationalities_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Nationalities option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
   #Validate title of the page as CorporateBranding     
   def check_CorporateBranding_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("CorporateBranding option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
   #Validate title of the page as Configuration     
   def check_Configuration_by_xpath(self):
        fullXPath = "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span"
        try:
            element = self.driver.find_element(by=By.XPATH, value=fullXPath)
            sleep(10)
            print("Configuration option is displaying on admin page")
        except NoSuchElementException:
            return False
        return True
       
   def quit(self):
       self.driver.quit()

   
   
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
obj.check_OrangeHRM_by_xpath()
obj.check_UserManagement_by_xpath()
obj.check_Job_by_xpath()
obj.check_Organization_by_xpath()
obj.check_Qualifications_by_xpath()
obj.check_Nationalities_by_xpath()
obj.check_CorporateBranding_by_xpath()
obj.check_Configuration_by_xpath()
obj.quit()