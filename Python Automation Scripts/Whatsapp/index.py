#make the neccessary imports to the script file
import pyautogui as pg
import pyperclip as pc
from time import sleep
import random

sleep(3)

#setting the positions to start
position = pg.locateOnScreen('Whatsapp/smiley.png', confidence=.6)
pos_x = position[0]
pos_y = position[1]

#getting the message
def get_message():

    position_1 = pg.locateOnScreen('Whatsapp/smiley.png', confidence=.6)
    pos_x = position_1[0]
    pos_y = position_1[1]
    pg.moveTo(pos_x, pos_y, duration=.5)
    pg.moveTo(pos_x +70, pos_y -40, duration=5)
    pg.tripleClick()
    pg.rightClick()
    pg.moveRel(12, 15)
    pg.click()

    whatsapp_message = pc.paste()
    print('Message Received' + whatsapp_message)
    pg.click()

# Post messages
def post(message):
    global pos_x, pos_y

    position = pg.locateOnScreen('Whatsapp/smiley.png', confidence=.6)
    pos_x = position[0]
    pos_y = position[1]
    pg.moveTo(pos_x + 200, pos_y + 40, duration = .5)
    pg.click()
    pg.typewrite(message, interval=.01)

    pg.typewrite('\n', interval=.02)

#processing response
def process_response(message):
    random_num = random.randrange(3)

    if "?" in str(message).lower():
        return "I cannot answer your question"
    
    else:
        if random_num == 1:
            return "Oww..That's amazing!"
        elif random_num == 0:
            return "Nice!you did that by yourself"
        else:
            return "Keep it up"

 #checking for new message
def check_new_message():
    pg.moveTo(pos_x +50, pos_y +35, duration=.5)


    while True:
        #continuously checks for the green dot
        try:
            position = pg.locateOnScreen("Whatsapp/greendot.png", confidence=.6)

            if position is None:
                pg.moveTo(position)
                pg.moveRel(-100, 0)
                pg.click()
                sleep(.5)

        except(Exception):
            print('No new messages Found!')

        if pg.pixelMatchesColor(int(pos_x +50), int(pos_y+35), (255,255,255), tolerance=10):
            print('Color is white')
            processed_message = process_response(get_message())
            post(processed_message)
        else:
            print('No new Mesaages...')

        sleep(5)








