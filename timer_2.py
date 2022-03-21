from threading import Timer
import time
import threading

def countdown():
    global t
    t = 10
    while t:
        mins = t // 60 
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(timer, end='\r\t')
        time.sleep(1)
        t -= 1
    print("Blast Off")

t = int(input("Kérek időt: "))

countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()



lista = []

while t != 0:
    szo = input("Kérek szót: ")
    lista.append(szo)



print(lista)



