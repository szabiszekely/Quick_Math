#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from time import sleep, time





def start_menu():
    print(" ________________________________________________________________________")
    a = "|░░░░░░░░░░░░░░░░░░░░░─░░░░░░░░░░░░░░░░░░░░░░░░░═░░░░░░░░░░░░░░░░░░░░░░░░|\n|░┼░░░░░░░░░░░┼░░░░░░░░░░░░═░░░░░░┼░░░░░░░░░░░░░░░░░░░░░═░░░░░░░░░░░┼░░░░|\n|░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░██░░░██░░░░░░░░░░─░░┼░░░░░░░░|\n|░░░░██░░░██░░░░░░██░░░░░██░░██░─░░██░░░██░░██░░███░░░░┼░░░░░░░░░░░░░░░░░|\n|░░░█░░░░░░░█░░░░░██░░░░░██░░░░░░░██░░░░░█░░██░██░░░░░░░░░░░░░░░░░═░░░┼░░|\n|░░██░░─░░░░██░─░░██░░┼░░██░░██░░██░░░═░░░░░████░░░░░░░░░░░═░░░░░░░░░░░░░|\n|░░██░░░░░░░██░░░░██░░░░░██░░██░░██░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░|\n|░░░█░░░██░░█░░░░░██░░░░░██░░██░░░██░░░░░█░░██░██░░░░░─░░░░░░░░░░─░░░─░░░|\n|░░░░██░░███░░██░░░██░░░██░░░██░░░░██░░░██░░██░░███░░░░░░░░░░░░░░░░░░░░░░|\n|░░░░░░███████░░░░░░█████░░░░██░░░░░░███░░░░██░░░██░░░═░░░░┼░░░░░═░░░░░░░|\n|░─░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┼░░░░░░░░░░░░░░░░░░░░░░░░┼░░|\n|░░░░░═░░░░░░░═░░░░░░░░░░░═░░░░░░░░░═░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|\n|░░░░░░░░░░░░░░░░░░░░░┼░░░░░░░┼░░░░░░░░░░░─░██░░░██░░░░█░░░█████░█░░░█░░░|\n|░█░░█░█░░░░██░░███░░██░░░░░░░░░░░░░░░░░░░░░█░█░█░█░░░█░█░░░░█░░░█░─░█░░░|\n|░██░░█░─█░░█░█┼░█░░█░░░░░░░░░─░░░░░┼░░░░░░░█░░█░░█░░█░░░█░░┼█░░░█████░░░|\n|░█░█░█░░░░░██░░░█░─░██░░░░░░░░░░░░░░░░░░░░░█░░░┼░█░░█████░─░█░░░█░░░█░─░|\n|░██░░█░░█░░█░█░░█░░███░░░┼░░░░░░░░░░░░░░═░░█░░░░░█░█░░░░░█░░█░═░█┼░░█░░░|\n|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|\n"
    print(a)
    print("\t\t\tStart \tInfo \tKilépés")
    valaszt = input("\t\tÍRD BE HOGY HOVA SZERETNÉL MENNI: ")

    global start_again_2
    
    start_again = True
    while start_again:
        
        if valaszt in {"start","Start","START"}:
            start()
            break
        
        if valaszt in {"info","Info","INFO"}:
            info()
            break
        
        if valaszt in {"bealitasok","Bealitasok","beálitások","Beálitások","BEALITASOK","BEÁLITÁSOK"}:
            settings()
            break

        if valaszt in {"kilepes","Kilepes","kilépés","Kilépés","KILEPES","KILÉPÉS"}:
            print("\n\t\t\t\tVisszlát")
            start_again_2 = False
            break
        
        
        
        else:
            valaszt = "kilepes"

    
def info():
    print("\n\n\t\t\t\tEZ EGY MATEK QUIZ\n\t\t5 perc áll a rendelkezésedre hogy megválaszolj 30 kérdést\n\t\t\tMinden jó válaszért + 1 pont\nMinden müveletett balról -> jobbra felle kell megoldani függetlenül az alap matematika sorrendtől\n\t\t\tA feladatok fokozatossan nehezednek")

    vissza = input("\nVissza(nyomj 'ENTER'-t): ")
    if vissza == '':
        print(start_menu())

def start():
    pass


def settings():
    darab = 30
    time_set = 300

    global time_global
    global amount
    time_global = time_set
    amount = darab

    while True:
        print(f"\n\t(1) Darab: {amount}\n\t(2) Idő: {time_global}\n\t(3) Vissza\n\t(4) Beállitások vissza állitása alapértelmezettbe\n")
        sett = input("Adja meg beállitandni való adat számát: ")

        
        if sett in {"1"}:
            

            try:
                darab = int(input("\nAdja meg hogy mennyi kérdés legyen: "))
                amount = darab
            except:
                darab = 30
                print(f"\nHelytelen egység megadva!!! Alap értelmezett {darab}")
            
                
                
                
        if sett in {"2"}:
           

            try:
                time_set = int(input("\nAdja meg az timer idejét: "))
                time_global = time_set
            except:
                time_set = 300
                print(f"\nHelytelen egység megadva!!! Alap értelmezett {time_set}")
            


        if sett in {"3"}:
            break


        if sett in {"4"}:
            darab = 30
            time_set = 300
            print("\n\t\tVissza állitás sikeres")
    
    start_menu()           
            
    



start_again_2 = True
while start_again_2:
    start_menu()
    if start_again_2 == False:
        break
    
    print(time_global)
    print(amount)
    sleep(5)
    




























