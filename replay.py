# -*- coding: cp950 -*-
import time
import os
import sys
import pyautogui

os.chdir(os.path.dirname(os.path.realpath(__file__)))
directory = 'mouse_recorder'
try:
    session_name = 'helloworld' # sys.argv[1]
except:
    print ('you must enter a name for the session\nfor example: python replay.py session_name')
    sys.exit()
dir_path = os.path.join(os.getcwd(), directory, session_name)

file_name = 'history.txt'
file_path = os.path.join(dir_path, file_name)
#print dir_path

print(file_path)
# open the recording file
with open(file_path, 'r') as f:
    steps = f.readlines()

print('-'.join(['# of steps', str(len(steps))]))
# clean steps
new_steps = []
for step in steps:
    new_step = []
    for i in step.split(','):
        new_step.append(i.strip('\n'))
        #print(new_step[-1])
    #print('.'.join(['new_step', new_step]))
    new_steps.append(new_step)


# start moving mouse cursor
t_last = float(new_steps[0][-1])

for step in new_steps:

    print(step[0])
    if step[0] == 'mouse left down':
        
        time.sleep(float(step[-1]) - t_last)
        print('.'.join(['moveto', step[2],step[3]]))
        pyautogui.moveTo(int(step[2]), int(step[3]))
        pyautogui.mouseDown(button='left')
        t_last = float(step[-1])

    if step[0] == 'mouse left up':
        time.sleep(float(step[-1]) - t_last)
        print('.'.join(['moveto', step[2],step[3]]))
        pyautogui.moveTo(int(step[2]), int(step[3]))
        pyautogui.mouseUp(button='left')
        t_last = float(step[-1])

    if step[0] == 'mouse right down':
        time.sleep(float(step[-1]) - t_last)
        pyautogui.moveTo(int(step[2]), int(step[3]))
        pyautogui.mouseDown(button='right')
        t_last = float(step[-1])

    if step[0] == 'mouse right up':
        time.sleep(float(step[-1]) - t_last)
        pyautogui.moveTo(int(step[2]), int(step[3]))
        pyautogui.mouseUp(button='right')
        t_last = float(step[-1])

    if step[0] == 'done':
        print ('End autorun')
        sys.exit()
