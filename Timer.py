import time
import sys
from math import ceil

timeStr = input("Welcome to Timer\nEnter a time amount in 1h15m34s: ")

hr = timeStr.find('h')
min = timeStr.find('m')
sec = timeStr.find('s')

loop = 0
   
if sec != -1:
    
    sec = timeStr[min+1:sec]
    
    loop += int(sec)
        
if min != -1:
    
    min = timeStr[hr+1:min]
    
    loop += int(min)*60
    
if hr != -1:
    
    hr = timeStr[:hr]

    loop += int(hr)*3600

print(hr, min, sec)

print(loop)

print("Entering Timer!\n\n\n")

for i in range(loop):
    print(f'\r{i}/{loop}')
    
    print('[', end='')
    
    j = ((i/loop)*100)/3
    j = ceil(j)+1
    
    for j in range(j): 
        print("=", end = "")
    
    print('>', end='')
    
    spaces = 33-j

    for spaces in range(spaces):
        print(' ', end = '')
        
    print(']', end='', flush=True)

    time.sleep(1)
    
    print('\033[F                                                                            ', end='')
    
print('TIMER ENDED')




