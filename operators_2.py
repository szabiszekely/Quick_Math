from calendar import c
import operator
import random

def eloszto(kor):
    
    if 10 < kor <= 15:
        result = op_hordo_10_15()

    if 5 < kor <= 10:
        result = op_hordo_5_10()
        
    if kor <= 5:    
        result = op_hordo_1_5()
        
    return result

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





#-----------------------------------------------------------------------------------------    






talalat = 0
kor = 1
while kor <= 15:

    vegeredmeny = eloszto(kor)


    print("oOoOoOooOoOoOo")
    
    print("Kör: ",kor)
    if kor <= 10:
        muvelet = int(input(f"{a} {string_op_1} {b} = "))
    elif 10 < kor <= 15:
        muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} = "))

    if vegeredmeny == muvelet:
        kor += 1
        talalat += 1
    else:
        kor += 1

print("Találatok száma: ",talalat)


