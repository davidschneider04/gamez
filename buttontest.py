import board
from digitalio import DigitalInOut, Direction, Pull
import time



#gnd: 39
#io: 35
#3v: 17

button_white = DigitalInOut(board.D19)
button_white.direction = Direction.INPUT
button_white.pull = Pull.UP
button_blue = DigitalInOut(board.D20)
button_blue.direction = Direction.INPUT
button_blue.pull = Pull.UP
button_red = DigitalInOut(board.D26)
button_red.direction = Direction.INPUT
button_red.pull = Pull.UP
button_yellow = DigitalInOut(board.D13)
button_yellow.direction = Direction.INPUT
button_yellow.pull = Pull.UP
button_black = DigitalInOut(board.D6)
button_black.direction = Direction.INPUT
button_black.pull = Pull.UP
button_green = DigitalInOut(board.D21)
button_green.direction = Direction.INPUT
button_green.pull = Pull.UP
button_l1 = DigitalInOut(board.D22)
button_l1.direction = Direction.INPUT
button_l1.pull = Pull.UP
button_l2 = DigitalInOut(board.D27)
button_l2.direction = Direction.INPUT
button_l2.pull = Pull.UP
button_r1 = DigitalInOut(board.D18)
button_r1.direction = Direction.INPUT
button_r1.pull = Pull.UP
button_r2 = DigitalInOut(board.D17)
button_r2.direction = Direction.INPUT
button_r2.pull = Pull.UP
button_select = DigitalInOut(board.D23)
button_select.direction = Direction.INPUT
button_select.pull = Pull.UP
button_start = DigitalInOut(board.D24)
button_start.direction = Direction.INPUT
button_start.pull = Pull.UP

buttons = {'white': button_white
        ,'red': button_red
        ,'yellow': button_yellow
        ,'black': button_black
        ,'green': button_green
        ,'blue': button_blue
        ,'l1': button_l1
        ,'l2': button_l2
        ,'r1': button_r1
        ,'r2': button_r2
        ,'start': button_start
        ,'select': button_select}

while True:
    for key, val in buttons.items():
        if not val.value:
            print(key)
    time.sleep(0.01) 
