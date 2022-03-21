from glob import glob
from time import *
import threading
from traceback import print_tb

#ez def a számlálóhoz
def countdown():
    global my_timer
    
    my_timer = timer

    for x in range(timer):
        
        my_timer -= 1
        sleep(1)

#a countdown-t meghatárózó intervalum
timer = 10
#timer = int(input("Adja meg az időt(másodpercben): "))

countdown_thread = threading.Thread(target = countdown)
countdown_thread.start()


#minden más
lista = []
while my_timer > 0:
    
    szo = input("Kérek szót: ")
    lista.append(szo)

print(lista)    
print("\nTimes up")












