
import time
import os
import datetime
from colorama import Fore

def clearScreen():
    """
    only clear screen function
    :::work on unix and windows:::
    """
    if os.name == "nt":
        os.system("cls")
    else : 
        os.system("clear")


startTime = datetime.datetime.now().strftime("%H:%M:%S")
timer = ["00" , "00" , "00"]

hour = timer[0]
min = timer[1]
sec = timer[2]



while True : 
    now = datetime.datetime.now().strftime("%H:%M:%S")
    clearScreen()
    print()
    print(f"     Start : {startTime}")
    print(f"     Now : {now}")
    print(Fore.GREEN , f"      {hour}:{min}:{sec}" , Fore.RESET)
    time.sleep(1)


    """
    this condition block for check time shift
    if sec == 60 : 
        min = min + 1
        sec = 0
    if min == 60 :
        hour = hour + 1
        min = 0
    """
    #use str format for handle 00:00:00 format
    sec = str(int(sec) + 1)
    if sec == "60" : 
        min = str(int(min) + 1)
        sec = "0"
        
    if min == "60" : 
        hour = str(int(hour) + 1)
        min = "0"



    """
    this condition block for check time format 
    00:00:00
    timer[0] -> hour
    timer[1] -> min
    timer[2] -> sec
    """
    if len(sec) == 1 : 
        sec = "0" + sec
    if len(min) == 1 : 
        min = "0" + min
    if len(hour) == 1 : 
        hour = "0" + hour
