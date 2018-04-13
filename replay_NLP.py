import time
import os
import sys
import pyautogui
import nltk
import numpy


# Simple usage
from stanfordcorenlp import StanfordCoreNLP

stf_path = r'D:\Balaji\sharedfolder\nltk_rec\stanford-corenlp-full-2018-02-27'

if len(sys.argv) > 1:
    sentence = sys.argv[1]
    nlp = StanfordCoreNLP(stf_path)
    # sentence = "Send invoice to Optisol Inc., for amount of $1000 for work done on April 2018"
    named_entity =  nlp.ner(sentence)
    # print('Named Entities:', named_entity)
    nlp.close() # Do not forget to close! The backend server will consume a lot memery.

    temp = {}
    for i, entity in enumerate(named_entity):
        if entity[1] is not 'O':
            if entity[1] in temp:
                temp[entity[1]] = temp[entity[1]] + ' '+ entity[0]
            else:
                temp[entity[1]] = entity[0]
        else:
            if entity[0] == 'to' and "NAME" not in temp:
                temp["NAME"] = named_entity[i+1][0]
    print(temp)
    if "DATE" not in temp or "MONEY" not in temp:
        print("Try something like")
        print("'Send offerletter to Joe Smith for $500 on April 2018'")
    else:
        # print("Great! working out")
        sys.exit()

else:
    print("Please enter a sentence to continue!!!")
    exit()

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
specialkeys = ['Lcontrol','Lshift']
keytranslations = {'Oem_Minus' : '_',
                   'Lmenu': 'alt',
                   'Lcontrol': 'ctrl',
                   'Lshift' : 'shift'}

skipcount = 0
# skip = False
for i, step in enumerate(new_steps):
    print(step)
    sys.exit()
    if skipcount > 1:
        skipcount = skipcount - 1
        t_last = float(step[-1])
        continue
    print(step[0])
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
        
    if step[0] == 'done':
        print ('End autorun')
        sys.exit()
    
    
def trysomething():
    time.sleep(5)
    print('trying something')
    #pyautogui.hotkey('ctrl', 'a')
    pyautogui.keyDown('shift')
    pyautogui.keyDown('end')
    pyautogui.keyUp('end')
    pyautogui.keyUp('shift')