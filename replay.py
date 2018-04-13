# -*- coding: cp950 -*-
import time
import os
import sys
import pyautogui
import ParseHistory as ph


os.chdir(os.path.dirname(os.path.realpath(__file__)))
directory = 'mouse_recorder'
try:
    session_name = 'SendOfferLetter' # sys.argv[1]
except:
    print ('you must enter a name for the session\nfor example: python replay.py session_name')
    sys.exit()
dir_path = os.path.join(os.getcwd(), directory, session_name)

file_name = 'OfferLetterScripts.txt'
file_path = os.path.join(dir_path, file_name)
#print dir_path

print(file_path)
# open the recording file
with open(file_path, 'r') as f:
    steps = f.readlines()

steps = ph.parse()    
#for s in steps:
#    print (s)


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

for ns in new_steps:
    print(ns)
    
sys.exit()

# start moving mouse cursor
t_last = float(new_steps[0][-1])
specialkeys = ['Lcontrol','Lshift']
keytranslations = {'Oem_Minus' : '_',
                   'Lmenu': 'alt',
                   'Lcontrol': 'ctrl',
                   'Lshift' : 'shift'}

skipcount = 0
#skip = False
for i, step in enumerate(new_steps):
    print(step[0])
    if skipcount > 1 and step[0] != 'done':
        skipcount = skipcount - 1
        t_last = float(step[-1])
        continue

    if step[0] == 'mouse left down':
        
        time.sleep(float(step[-1]) - t_last)
        print('.'.join(['moveto', step[2],step[3]]))
        pyautogui.click(int(step[2]), int(step[3]))
        t_last = float(step[-1])

    if step[0] == 'key down':
        time.sleep(float(step[-1]) - t_last)
        if(step[2] in specialkeys):
            print(step[2].lower())
            if(step[2] in keytranslations):
                specialkey = keytranslations[step[2]]
            #specialkey = 'ctrl'
            #if(step[2] == 'Lshift'):
            #    specialkey = 'shift'p
            nextkey = specialkey
            skipcount = 1
            while nextkey == specialkey:
                nextkey = new_steps[i+skipcount][2] 
                skipcount = skipcount + 1
            
            print(','.join([specialkey,nextkey.lower()]))
            pyautogui.hotkey(specialkey, nextkey.lower())
            t_last = float(step[-1])
            #skip = True
        else:
            if(step[2] in keytranslations):
                step[2] = keytranslations[step[2]]
            pyautogui.hotkey(step[2].lower())
            print(step[2].lower())
        t_last = float(step[-1])
        
    #key sys down,hello - Notepad,Lmenu,55.25,1523539773.901936
    if(step[0] == 'key sys down'):
        time.sleep(float(step[-1]) - t_last)
        if(step[2] in keytranslations):
            step[2] = keytranslations[step[2]]
        pyautogui.hotkey(step[2].lower())
        print(step[2].lower())
        t_last = float(step[-1])
    
    if(step[0] == 'type write'):
        pyautogui.typewrite(step[1], interval=0.05)
        
    if (step[0] == 'done'):
        print ('End autorun')
        sys.exit()

sys.exit()
    
