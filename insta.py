from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from PySimpleGUI import PySimpleGUI as sg


class InstagramBot:
    def __init__(self, amount):
        self.amount = amount
        self.driver = webdriver.Firefox(
            executable_path=r"./geckodriver.exe.exe")

        sg.theme('Reddit')
        layout = [
            [sg.Text('Usuario:'), sg.Input(size=(15,0),key= 'usuario')],
            [sg.Text('Senha:'), sg.Input(size=(15,0),key= 'senha', password_char='*')],
            [sg.Text('Link do Sorteio:'), sg.Input(size=(15,0),key= 'link')],
            [sg.Text('Comentario:'), sg.Input(size=(15,0),key= 'comentario')],
            [sg.Button('Comentar')],
            [sg.Output(size=(30,10))]
        ]

        janela = sg.Window('Tela de login', layout, icon=r'./robot.ico')
        self.eventos, self.valores = janela.read()
        self.link = self.valores['link']

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except:
            print(f'já estamos na página de login')
            pass

        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.valores['usuario'])
        time.sleep(random.randint(1, 3))
        
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.valores['senha'])
        time.sleep(random.randint(1, 3))
        password_element.send_keys(Keys.RETURN)
        
        time.sleep(random.randint(3, 5))
        
        self.comment(self.valores['link'])
         
    def start(self):
        while True:
            if self.eventos == sg.WINDOW_CLOSED:
                break
            self.login()
            

    #@staticmethod
    def type_like_a_person(self, single_input_field):
        for letter in self.valores['comentario']:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comment(self, sorteio):
        driver = self.driver
        driver.get(sorteio)
        exe = 0
        while exe < self.amount:
            comment_area = driver.find_element_by_class_name("Ypffh")
            comment_area.click() 
            time.sleep(1)
            comment_area = driver.find_element_by_class_name("Ypffh")
            self.type_like_a_person(comment_area)
            comment_area.send_keys(Keys.RETURN)
            exe+=1
            time.sleep(random.randint(20, 45))
            print(exe)
            
InstagramBot(1000000).start()