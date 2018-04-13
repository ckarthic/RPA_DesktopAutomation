# -*- coding: cp950 -*-
import time
import os
import sys
import pyautogui

def parse(params_ = [{'param': 'cname', 'text': 'karthic chandran'},
                     {'param': 'cdate', 'text': 'April 2008'},
                     {'param': 'camount', 'text':  '10000'}]):
    #os.chdir(os.path.dirname(os.path.realpath(__file__)))
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
    
    

    keytranslations = {'Oem_Minus' : '_',
                       'Lmenu': 'alt',
                       'Lcontrol': 'ctrl',
                       'Lshift' : 'shift',
                       'Space' : ' '}
    params = ['cname','cdate','camount']
    specialkwds = ['Return', 'Tab']
    
    
    keywordArray = []
    keywordDict = {}
    typedtxt = ''
    skipParse = False
    lineCount = -1
    for i, step in enumerate(new_steps):
        lineCount = lineCount + 1
        if skipParse:
            skipParse = False
            continue
        if(step[0] == 'key down'):
            if(step[2] not in specialkwds):
                if(step[2] in keytranslations):
                    step[2] = keytranslations[step[2]]
                if(step[2] == 'ctrl'):
                    skipParse = True
                    continue
                if(typedtxt == ''):
                    #print(lineCount)
                    keywordDict['start'] = lineCount
                typedtxt = typedtxt + step[2]
            else:
                #print(step[2])
                if(typedtxt != ''):
                    #keywords.append(typedtxt)
                    keywordDict['text'] = typedtxt
                    keywordArray.append(keywordDict.copy())
                    keywordDict = {}
                typedtxt = ''
       
        continue
    
    print('\nprinting extracted text \n')
    for i, k in enumerate(keywordArray):
        print(k)
        
    print('\nKeywordArray\n')
    for k in keywordArray:
        print(k)
        
    replaceLines = []
    for i, k in enumerate(keywordArray):
        #print(','.join([k['text'], str(k['start'])]))
        if(k['text'].lower() in params):
            keywordArray[i+1]['param'] = k['text'].lower()
            replaceLines.append(keywordArray[i+1])
            #print(','.join([nextPos['text'], str(nextPos['start'])]))

    print('\nreplacelines\n')            
    for l in replaceLines:
        print(l)
    
    #stripedSteps = []
    #stripedSteps = stripedSteps + steps[:16]
    #stripedSteps = stripedSteps + steps[26:38]
    #stripedSteps = stripedSteps + steps[49:63]
    #stripedSteps = stripedSteps + steps[68:114]
            
    stripedSteps = []
    for i, r in enumerate(replaceLines):
        print(i)
        if(i == 0):
            b = 0
            e = r['start']
            print(':'.join([str(b), str(e)]))
            stripedSteps = stripedSteps + steps[b:e]
        else:
            b = replaceLines[i-1]['start'] + len(replaceLines[i-1]['text'])
            e = r['start']
            print(':'.join([str(b), str(e)]))
            stripedSteps = stripedSteps + steps[b : e]
        insertline = 'type write, ' + params_[i]['text']
        stripedSteps.append(insertline)
        
    b = replaceLines[-1]['start'] + len(replaceLines[-1]['text'])
    e = len(steps) + 1
    print(':'.join([str(b), str(e)]))
    stripedSteps = stripedSteps + steps[b : e]
            
    #for s in stripedSteps:
    #    print(s.replace('\n',''))
        
    return stripedSteps
    
def trysomething():
    time.sleep(5)
    print('trying something')
    pyautogui.typewrite('karthic chandran', interval=0.05)
    #pyautogui.hotkey('ctrl', 'a')
    #pyautogui.keyDown('shift')
    #pyautogui.keyDown('end')
    #pyautogui.keyUp('end')
    #pyautogui.keyUp('shift')
    
def LearnDict():
    keywordDict = {}
    keywordArr = []
    
    keywordDict['text'] = 'joe smith'
    keywordDict['start'] = 10
    keywordArr.append(keywordDict.copy())
    
    keywordDict = {}
    keywordDict['text'] = 'April 2018'
    keywordDict['start'] = 25
    keywordArr.append(keywordDict.copy())
    
    for k in keywordArr:
        print(','.join([k['text'], str(k['start'])]))
        
    
    
def SliceArray():
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
    
    stripedSteps = []
    stripedSteps = stripedSteps + steps[:16]
    stripedSteps = stripedSteps + steps[26:38]
    stripedSteps = stripedSteps + steps[49:63]
    stripedSteps = stripedSteps + steps[68:114]
    
    for s in stripedSteps:
        print(s.replace('\n',''))
    #stripedSteps = stripedSteps + steps[10:15]
    #del steps[16:24+1]
    
    #for s in stripedSteps:
    #    print(s)
    
    #for i, s in enumerate(steps):
    #    print('-'.join([str(i), s.replace('\n','')]))
        

    