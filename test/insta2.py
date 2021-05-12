from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from PySimpleGUI import PySimpleGUI as sg
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def login():
    sg.theme('Reddit')
    layout = [
            [sg.Text('Usuario:'), sg.Input(size=(15, 0), key= 'usuario')],
            [sg.Text('Senha:'), sg.Input(size=(15, 0), key= 'senha', password_char='*')],
            [sg.Text('Link do Sorteio:'), sg.Input(size=(15, 0), key= 'link')],
            [sg.Text('Comentario:'), sg.Input(size=(15, 0), key= 'comentario')],
            [sg.Button('Comentar')],
            [sg.Output(size=(30, 10))]
    ]

    janela = sg.Window('Tela de login', layout, icon=r'./robot.ico')
    eventos, valores = janela.read()
    link = valores['link']

    while True:
        if eventos == 'Comentar':
            print('comenta')
            driver = webdriver.Firefox(
                executable_path=r"./geckodriver.exe.exe")
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
            user_element.send_keys(valores['usuario'])
            time.sleep(random.randint(1, 3))

            password_element = driver.find_element_by_xpath(
                "//input[@name='password']")
            password_element.clear()
            password_element.send_keys(valores['senha'])
            time.sleep(random.randint(1, 3))
            password_element.send_keys(Keys.RETURN)

            time.sleep(random.randint(3, 5))

            driver.get(link)
            exe = 0
            while exe < 100000:
                comment_area = driver.find_element_by_class_name("Ypffh")
                comment_area.click()
                time.sleep(1)
                comment_area = driver.find_element_by_class_name("Ypffh")

                for letter in valores['comentario']:
                    comment_area.send_keys(letter)
                    time.sleep(random.randint(1, 5) / 30)
                    
                comment_area.send_keys(Keys.RETURN)
                exe += 1
                time.sleep(random.randint(20, 45))
                print(exe)
        

    






'''
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("cred.json", scope)
client = gspread.authorize(creds)
sheet = client.open("users").sheet1  
data = sheet.get_all_records()
'''
sg.theme('Reddit')
login = [
    [sg.Text("Email"), sg.Input(key='botmail')],
    [sg.Text("Senha"), sg.Input(key='botpass')],
    [sg.Button('Ir')],
    [sg.Output(size=(30, 10))]
]
janela_login = sg.Window(
    'Tela de login BOT', login, icon=r'./robot.ico')
eventos_bot, valores_bot = janela_login.read()

while True:
    if eventos_bot == sg.WINDOW_CLOSED:
        print('ir press')
        login()
        break

# @staticmethod



