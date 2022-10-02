import random
from sys import setswitchinterval

import pyautogui as pg
import time
words=("Hi")
time.sleep(8)

for i in range(5):
    a=random.choice(words)
    pg.write(a)
    pg.press('enter')