from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password, frase, amount):
        self.username = username
        self.password = password
        self.frase = frase
        self.amount = amount
        self.driver = webdriver.Firefox(
            executable_path=r"./geckodriver.exe.exe")  

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except:
            print('já estamos na página de login')
            pass

        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(random.randint(1, 3))
        
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(1, 3))
        password_element.send_keys(Keys.RETURN)
        time.sleep(4)

        driver.get("https://www.instagram.com/_melissatong/")

        comment_area = driver.find_element_by_xpath("//button[contains(text(),'Enviar mensagem')]");
        comment_area.click() 
        time.sleep(3)
        comment_area = driver.find_element_by_xpath("//button[contains(text(),'Agora não')]");
        comment_area.click() 
        time.sleep(2)
        
        self.comment()
        
        
         

    #@staticmethod
    def type_like_a_person(self, single_input_field):
        for letter in self.frase:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comment(self):
        driver = self.driver
        exe = 0
        while exe < self.amount:
            mes_area = driver.find_element_by_tag_name('textarea')
            self.type_like_a_person(mes_area)
            mes_area.send_keys(Keys.RETURN)
            exe+=1
            time.sleep(random.randint(1, 2))
            
        


meurobo = InstagramBot("gabriel_lemache", "meia07", "MELISSA OTAKU VOU LEVAR ELA PRO JAPAO", 100000)
meurobo.login()



   