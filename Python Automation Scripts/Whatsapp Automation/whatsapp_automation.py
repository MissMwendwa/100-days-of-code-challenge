#make the neccessary imports to the script file
import pyautogui as pg
import pyperclip as pc
from time import sleep
import os

# create the whatsapp instructions
class Whatsapp:

    #define the start point
    def __init__(self, speed=.5, click_speed=.3):
        self.speed= speed
        self.click_speed = click_speed
        self.messsage = ''
        self.last_message = ''

    #navigation to the new messages/ green messages
    def nav_green_dot(self):
        try:
            position = pg.locateOnScreen('greendot.png', confidence=.7)
            pg.moveTo(position, duration=self.speed)
            pg.moveRel(-100, 0, duration=self.speed)
            pg.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exceprtion(nav_green_dot): ', e)


# calling the function to perform the necessary activities
wa_bot = Whatsapp(speed = .5, click_speed=.4)

wa_bot.nav_green_dot()







