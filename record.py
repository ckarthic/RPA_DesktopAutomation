import time
import os
import sys
from functools import partial
import pyHook
import pythoncom
import pyautogui

def left_down(event, file_path, start = time.time()):
    #print(type(event))
    x, y = event.Position
    #print (",".join(['left_down', str(x), str(y)]))
    print(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))

    with open(file_path, 'a') as f:
        f.write(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))
        #f.write(",".join(['left_down', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True

def left_up(event, file_path, start = time.time()):
    x, y = event.Position
    #print (",".join(['left_up', str(x), str(y)]))
    print(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))
    with open(file_path, 'a') as f:
        f.write(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))
        #f.write(",".join(['left_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True

def right_down(event, file_path, start = time.time()):
    x, y = event.Position
    #print (",".join(['right_down', str(x), str(y)]))
    print(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))

    with open(file_path, 'a') as f:
        f.write(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))
        #f.write(",".join(['right_down', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True

def right_up(event, file_path, start = time.time()):
    x, y = event.Position
    #print (",".join(['right_up', str(x), str(y)]))
    print(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))

    with open(file_path, 'a') as f:
        f.write(','.join([ event.GetMessageName(), event.WindowName, str(x), str(y),
                    str(round(time.time() - start,2)), str(time.time()) ]))
        #f.write(",".join(['right_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True

def OnKeyboardEvent(event, file_path, dir_path, start = time.time()):
    if event.Ascii == 27: # Ascii('ESC')=27
        print ('End of recording')
        with open(file_path, 'a') as f:
            f.write('done\n')
            sys.exit()
    print(','.join([ event.GetMessageName(), event.WindowName, event.GetKey(),
                    str(round(time.time() - start,2)), str(time.time()) ]))
    with open(file_path, 'a') as f:
        f.write(','.join([ event.GetMessageName(), event.WindowName, event.GetKey(),
                        str(round(time.time() - start,2)), str(time.time()) ]))
        #f.write(",".join(['right_up', str(x), str(y), str(time.time())]))
        f.write('\n')
    return True


if __name__ == '__main__':
    print(os.path.dirname(os.path.realpath(__file__)))
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    directory = 'mouse_recorder'
  
    print(len(sys.argv))
    try:
        session_name = 'SendOfferLetter' #sys.argv[1]
    except:
        print ('you must enter a name for the session\nfor example: python record.py session_name')
        sys.exit()
    dir_path = os.path.join(os.getcwd(), directory, session_name)
    print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    
    file_name = 'OfferLetterScripts.txt'
    file_path = os.path.join(dir_path, file_name)
    print (file_path)

    start = time.time()

    ld = partial(left_down, file_path=file_path, start = start)
    lu = partial(left_up, file_path=file_path,  start = start)
    rd = partial(right_down, file_path=file_path,  start = start)
    ru = partial(right_up, file_path=file_path,  start = start)

    hm = pyHook.HookManager()
    hm.SubscribeMouseLeftDown(ld)
    hm.SubscribeMouseLeftUp(lu)
    hm.SubscribeMouseRightDown(rd)
    hm.SubscribeMouseRightUp(ru)
    hm.HookMouse()


    oke = partial(OnKeyboardEvent, file_path=file_path, dir_path=dir_path, start=start)
    
    hm.KeyDown = oke
    hm.HookKeyboard()

    #while True:
    #    pythoncom.PumpWaitingMessages()
    pythoncom.PumpMessages()

    hm.UnhookMouse()
    hm.UnHookKeyboard()
