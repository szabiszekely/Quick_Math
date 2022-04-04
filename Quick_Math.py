#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from time import sleep

from calendar import c
import operator
import random
from glob import glob
from time import *
import threading
from traceback import print_tb



darab = 30
time_set = 300
time_global = time_set
amount = darab

#timer
def countdown():
    global my_timer
    
    my_timer = time_global

    for x in range(time_global):
        
        my_timer -= 1
        sleep(1)



#start menu
def start_menu():
    print(" ________________________________________________________________________")
    a = "|░░░░░░░░░░░░░░░░░░░░░─░░░░░░░░░░░░░░░░░░░░░░░░░═░░░░░░░░░░░░░░░░░░░░░░░░|\n|░┼░░░░░░░░░░░┼░░░░░░░░░░░░═░░░░░░┼░░░░░░░░░░░░░░░░░░░░░═░░░░░░░░░░░┼░░░░|\n|░░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░███░░░░██░░░██░░░░░░░░░░─░░┼░░░░░░░░|\n|░░░░██░░░██░░░░░░██░░░░░██░░██░─░░██░░░██░░██░░███░░░░┼░░░░░░░░░░░░░░░░░|\n|░░░█░░░░░░░█░░░░░██░░░░░██░░░░░░░██░░░░░█░░██░██░░░░░░░░░░░░░░░░░═░░░┼░░|\n|░░██░░─░░░░██░─░░██░░┼░░██░░██░░██░░░═░░░░░████░░░░░░░░░░░═░░░░░░░░░░░░░|\n|░░██░░░░░░░██░░░░██░░░░░██░░██░░██░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░|\n|░░░█░░░██░░█░░░░░██░░░░░██░░██░░░██░░░░░█░░██░██░░░░░─░░░░░░░░░░─░░░─░░░|\n|░░░░██░░███░░██░░░██░░░██░░░██░░░░██░░░██░░██░░███░░░░░░░░░░░░░░░░░░░░░░|\n|░░░░░░███████░░░░░░█████░░░░██░░░░░░███░░░░██░░░██░░░═░░░░┼░░░░░═░░░░░░░|\n|░─░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░┼░░░░░░░░░░░░░░░░░░░░░░░░┼░░|\n|░░░░░═░░░░░░░═░░░░░░░░░░░═░░░░░░░░░═░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|\n|░░░░░░░░░░░░░░░░░░░░░┼░░░░░░░┼░░░░░░░░░░░─░██░░░██░░░░█░░░█████░█░░░█░░░|\n|░█░░█░█░░░░██░░███░░██░░░░░░░░░░░░░░░░░░░░░█░█░█░█░░░█░█░░░░█░░░█░─░█░░░|\n|░██░░█░─█░░█░█┼░█░░█░░░░░░░░░─░░░░░┼░░░░░░░█░░█░░█░░█░░░█░░┼█░░░█████░░░|\n|░█░█░█░░░░░██░░░█░─░██░░░░░░░░░░░░░░░░░░░░░█░░░┼░█░░█████░─░█░░░█░░░█░─░|\n|░██░░█░░█░░█░█░░█░░███░░░┼░░░░░░░░░░░░░░═░░█░░░░░█░█░░░░░█░░█░═░█┼░░█░░░|\n|░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░|\n"
    print(a)
    print("\t\tStart \tInfo \tBeállitások\tKilépés")
    print("\t\t---------------------------------------\t")
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
        
        if valaszt in {"beallitasok","Beallitasok","beállitások","Beállitások","BEALLITASOK","BEÁLLITÁSOK"}:
            settings()
            break
        
        if valaszt in {"kilepes","Kilepes","kilépés","Kilépés","KILEPES","KILÉPÉS","x","X"}:
            print("\n\t\t\t\tVisszlát")
            start_again_2 = False
            break

        else:
            start_menu()


#minden ami az info szekciohoz hogyy müködjön
def info():
    print("\n\n\t\t\t\tEZ EGY MATEK QUIZ\n5 (tetszőlegessen lehet változtatni) perc áll a rendelkezésedre hogy megválaszolj 30 (tetszőlegessen lehet változtatni) kérdést.\n\t\t\tMinden jó válaszért + 1 pont.\nMinden müveletett balról -> jobbra felle kell megoldani függetlenül az alap matematika sorrendtől.\n\t\t\tA feladatok fokozatossan nehezednek.\nA '*' jelöli a szorzást, '/' jelöli az osztást és '**' jelöli ha valami a másodikon van.\n\t\t(pl: 10 ** 2 = 100 tíz a másodikon egyenlő kétszáz).\n\tA menűben lehet változtatni időt vagy kérdés számot ha esetleg kell.\n\t    Kérdés mennyiség nem leh 30-nál kevessebb, idő nem lehet minusz.")

    vissza = input("\nVissza(nyomj 'ENTER'-t): ")
    if vissza == '':
        print(start_menu())

#start szekció
def start():
    countdown_thread = threading.Thread(target = countdown)
    i = 3
    while i != 0:
        print(i)
        i -= 1
        sleep(1)
    global talalat
    global kor
    talalat = 0
    kor = 1
    print("GO")
    countdown_thread.start()


#a beállitásokkal foglalkozó szekció
def settings():
    darab = 30
    time_set = 300

    while True:
        global time_global
        global amount
        time_global = time_set
        amount = darab
        
        print(f"\n\t(1) Darab: {amount}\n\t(2) Idő: {time_global}\n\t(3) Vissza\n\t(4) Beállitások vissza állitása alapértelmezettbe\n")
        sett = input("Adja meg beállitandni való adat számát: ")

        #hány kérdés legyen
        if sett in {"1"}:
            
            try:
                darab = int(input("\nAdja meg hogy mennyi kérdés legyen: "))

                
            except:
                darab = 30
                print(f"\nHelytelen egység megadva!!! Alap értelmezett {darab}")
                
            if darab < 30:
                darab = 30

        #mennyi ideig tartson         
        if sett in {"2"}:
           

            try:
                time_set = int(input("\nAdja meg az timer idejét: "))
                
            except:
                time_set = 300
                print(f"\nHelytelen egység megadva!!! Alap értelmezett {time_set}")
            if time_set <= 0:
                time_set = 300
                
            

        #vissza a fő menübe
        if sett in {"3"}:
            break

        #Factory reset
        if sett in {"4"}:
            darab = 30
            time_set = 300
            print("\n\t\tVissza állitás sikeres")
    
    start_menu()           




#eloszto ez felell arra hogy fokozatos nehézségben jöjenek a kérdések
def eloszto(kor):
    
    if 25 < kor <= amount:
        result = op_hordo_25_30()

    if 20 < kor <= 25:
        result = op_hordo_20_25()

    if 15 < kor <= 20:
        result = op_hordo_15_20()

    if 10 < kor <= 15:
        result = op_hordo_10_15()

    if 5 < kor <= 10:
        result = op_hordo_5_10()
        
    if kor <= 5:    
        result = op_hordo_1_5()
        
    
    return result


# a matek feladványokra felelő rész ötösévvel renezve nehezedik 1 - 30-ig vagy tovvább
#............................................

# 1 - 5
def op_hordo_1_5():
    
    #define operators you wanna use
    allowed_operators_1={
    "+": operator.add,
    "-": operator.sub,}
    
    #sample variables
    global a
    a = random.randint(1,10)
    #print(a)
    
    global b
    b = random.randint(1,10)
    #print(b)
    
    lista_1 = ["+","-"]
    global string_op_1
    string_op_1 = random.choice(lista_1)
    #print(string_op_1)
    
    
    
    #sample calculation => a+b
    result = allowed_operators_1[string_op_1](a,b)
    
    #print(result)
    return result

# 5 - 10

def op_hordo_5_10():
    
    #define operators you wanna use
    allowed_operators_2={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}
    
    #sample variables
    global a
    a = random.randint(1,20)
    #print(a)
    
    global b
    b = random.randint(1,20)
    #print(b)
    
    lista_1 = ["+","-","*","/"]
    global string_op_1
    string_op_1 = random.choice(lista_1)
    #print(string_op_1)
    
    #sample calculation => a+b
    result = allowed_operators_2[string_op_1](a,b)
    #print(result)
    
    if not result % 1 == 0:
        #print("IGEN")
        while not result % 1 == 0:
            a = random.randint(1,20)
            b = random.randint(1,20)
            #print("-----")
            #print(a)
            #print(b)
            result = allowed_operators_2[string_op_1](a,b)
            
            #print(result)
    return result


#............................................
# 10 - 15

def op_hordo_10_15():
    
    #define operators you wanna use
    allowed_operators_3={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}
    
    #sample variables
    global a
    a = random.randint(1,20)
    #print(a)
    
    global b
    b = random.randint(1,20)
    #print(b)

    global c
    c = random.randint(1,20)
    #print(c)

    lista_1 = ["+","-","*","/"]
    global string_op_1
    string_op_1 = random.choice(lista_1)
    #print(string_op_1)

    lista_2 = ["+","-","*"]
    global string_op_2
    string_op_2 = random.choice(lista_2)
    
    #sample calculation => a+b
    elso = allowed_operators_3[string_op_1](a,b) 
    result = allowed_operators_3[string_op_2](elso,c)
    #print(result)
    
    if not result % 1 == 0:
        #print("IGEN")
        while not result % 1 == 0:
            a = random.randint(1,20)
            b = random.randint(1,20)
            c = random.randint(1,20)
            #print("-----")
            #print(a)
            #print(b)
            elso = allowed_operators_3[string_op_1](a,b) 
            result = allowed_operators_3[string_op_2](elso,c)
            
            #print(result)
    return result

# 15 - 20

def op_hordo_15_20():
    
    #define operators you wanna use
    allowed_operators_4={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}
    
    #sample variables
    global a
    a = random.randint(1,30)
    #print(a)
    
    global b
    b = random.randint(1,30)
    #print(b)

    global c
    c = random.randint(1,30)
    #print(c)

    lista_1 = ["-","/"]
    global string_op_1
    string_op_1 = random.choice(lista_1)
    #print(string_op_1)

    lista_2 = ["+","*"]
    global string_op_2
    string_op_2 = random.choice(lista_2)
    
    #sample calculation => a+b
    elso = allowed_operators_4[string_op_1](a,b) 
    result = allowed_operators_4[string_op_2](elso,c)
    #print(result)
    
    if not result % 1 == 0:
        #print("IGEN")
        while not result % 1 == 0:
            a = random.randint(1,30)
            b = random.randint(1,30)
            c = random.randint(1,30)
            #print("-----")
            #print(a)
            #print(b)
            elso = allowed_operators_4[string_op_1](a,b) 
            result = allowed_operators_4[string_op_2](elso,c)
            
            #print(result)
    return result


#............................................
# 20 - 25

def op_hordo_20_25():
    
    #define operators you wanna use
    allowed_operators_5={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "**": operator.pow}
    
    #sample variables
    global a
    a = random.randint(1,30)
    #print(a)
    
    global b
    b = random.randint(1,30)
    #print(b)

    global c
    c = 2
    #print(c)

    lista_1 = ["+","-","*"]
    global string_op_1
    string_op_1 = random.choice(lista_1)
    #print(string_op_1)

    lista_2 = ["**"]
    global string_op_2
    string_op_2 = random.choice(lista_2)
    
    #sample calculation => a+b
    elso = allowed_operators_5[string_op_1](a,b) 
    result = allowed_operators_5[string_op_2](elso,c)
    #print(result)
    
    if not result % 1 == 0:
        #print("IGEN")
        while not result % 1 == 0:
            a = random.randint(1,30)
            b = random.randint(1,30)
            c = random.randint(1,30)
            #print("-----")
            #print(a)
            #print(b)
            elso = allowed_operators_5[string_op_1](a,b) 
            result = allowed_operators_5[string_op_2](elso,c)
            
            #print(result)
    return result

# 25 - 30

def op_hordo_25_30():
    
    #define operators you wanna use
    allowed_operators_6={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow}
    
    #sample variables
    global a
    a = random.randint(1,50)
    #print(a)
    
    global b
    b = random.randint(1,50)
    #print(b)

    global c
    c = random.randint(1,50)
    #print(c)

    global d
    d = random.randint(2,3)
    #print(c)

    lista_1 = ["+","*"]
    global string_op_1
    string_op_1 = random.choice(lista_1)
    #print(string_op_1)

    lista_2 = ["-","/"]
    global string_op_2
    string_op_2 = random.choice(lista_2)

    lista_3 = ["**"]
    global string_op_3
    string_op_3 = random.choice(lista_3)
    
    #sample calculation => a+b
    elso = allowed_operators_6[string_op_1](a,b)
    masodik = allowed_operators_6[string_op_2](elso,c)
    result = allowed_operators_6[string_op_3](masodik,d)
    #print(result)
    
    if not result % 1 == 0:
        #print("IGEN")
        while not result % 1 == 0:
            a = random.randint(1,50)
            b = random.randint(1,50)
            c = random.randint(1,50)
            d = random.randint(2,3)
            #print("-----")
            #print(a)
            #print(b)
            elso = allowed_operators_6[string_op_1](a,b)
            masodik = allowed_operators_6[string_op_2](elso,c)
            result = allowed_operators_6[string_op_3](masodik,d)
            
            #print(result)
    return result

#-----------------------------------------------------------------------------------------    

darab = 30
time_set = 300
time_global = time_set
amount = darab






#ez felel arra hogy úra játszható legyen
start_again_2 = True
while start_again_2:
    start_menu()
    if start_again_2 == False:
        break


    # ha a kör = a max kérdésel vagy ha az idő = 0
    while kor <= amount + 1 or my_timer > 0:
        if my_timer == 0:
            print("Times up")
            print(f"Találataid száma: {talalat}/{kor}\n\n")
            sleep(5)
            break


        vegeredmeny = eloszto(kor)


        print("oOoOoOooOoOoOo")
        
        print("Kör: ",kor)
        
        if kor <= 10:
            try:
                muvelet = int(input(f"{a} {string_op_1} {b} = "))
            except:
                try:
                    muvelet = int(input(f"{a} {string_op_1} {b} = "))
                except:
                    muvelet = 1
        if 10 < kor <= 25:
            try:
                muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} = "))
            except:
                try:
                    muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} = "))
                except:
                    muvelet = 1
        
        if 25 < kor <= amount:
            try:
                muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} {string_op_3} {d} = "))    
            except:
                try:
                    muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} {string_op_3} {d} = "))    
                except:
                    muvelet = 1
        if kor == amount:
            break

        if vegeredmeny == muvelet:
            kor += 1
            talalat += 1
        else:
            kor += 1    
        
    if kor == amount:
        print(f"Gratulálok meg válaszoltad mind a {amount} matek feladványt időben")
        print(f"Találataid száma: {talalat}/{kor}")
        sleep(5)












































