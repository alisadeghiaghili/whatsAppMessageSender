import time
import webbrowser as web
import pyautogui as pg

def sendTimedWhatMsg(phoneNo, message, H, M, how = 'ontime'):
    '''Sends whatsapp message to specified number at given time'''
    if how == 'ontime':
        if H == 0:
            H = 24
            
        runTimeInSecs = H * 3600 + M * 60

        now = time.localtime()
        nowH = now.tm_hour
        nowM = now.tm_min
        nowS = now.tm_sec

        nowInSecs = nowH * 3600 + nowM * 60 + nowS
        timeLeft = runTimeInSecs-nowInSecs

        #set it for tomorrow
        if timeLeft <= 0:
            timeLeft += 24 * 3600

        if timeLeft < 60:
            raise Exception("Call time must be greater than one minute")

        else:
            sleepTime = timeLeft - 60
            time.sleep(sleepTime)
            web.open('https://web.whatsapp.com/send?phone=' + phoneNo + '&text=' + message)
            time.sleep(60)
            pg.press('enter')
    
    elif how == 'countdown':
        timeLeft = H * 3600 + M * 60
        
        if timeLeft < 60:
            raise Exception("Call time must be greater than one minute")

        else:
            sleepTime = timeLeft - 60
            time.sleep(sleepTime)
            web.open('https://web.whatsapp.com/send?phone=' + phoneNo + '&text=' + message)
            time.sleep(10)
            pg.press('enter')
            
def sendImmediateWhatMsg(phoneNo, message):
    '''Sends whatsapp message to specified number right now'''
    
    web.open('https://web.whatsapp.com/send?phone=' + phoneNo + '&text=' + message)
            time.sleep(10)
            pg.press('enter')
            
sendwhatmsg(phoneNo = input('enter the phone No'), 
            message = input('enter the message'), 
            how = input('ontime/countdown?'),
            H = int(input('enter the hour(s)')),
            M = int(input('enter the minute(s)')))