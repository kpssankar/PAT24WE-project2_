#Forgot password link validation on login page

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



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

   
   
   def login(self):
       self.boot()
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"))).click()
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input"))).send_keys("Admin")
       sleep(10)
       self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]"))).click()
       sleep(10)
       
       if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset":
               print("Reset password link sent successfully")
       else:
               print("Error in login")
               
obj = Form("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
obj.login()
obj.quit()

       