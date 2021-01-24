import time
import sys
from pynput.keyboard import Controller

keyboard = Controller()
file = open("plsbeg.txt", "r")
data = file.readlines()

time.sleep(7)

while 1 == 1:
    for i in data:
        keyboard.type(i)
        for remaining in range(46, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)


file.close()


