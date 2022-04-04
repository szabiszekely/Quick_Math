from calendar import c
import operator
import random

def eloszto(kor):
    
    if 25 < kor <= 30:
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






talalat = 0
kor = 1
while kor <= 30:

    vegeredmeny = eloszto(kor)


    print("oOoOoOooOoOoOo")
    
    print("Kör: ",kor)
    if kor <= 10:
        muvelet = int(input(f"{a} {string_op_1} {b} = "))
    elif 10 < kor <= 25:
        muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} = "))
    elif 25 < kor <= 30:
        muvelet = int(input(f"{a} {string_op_1} {b} {string_op_2} {c} {string_op_3} {d} = "))


    if vegeredmeny == muvelet:
        kor += 1
        talalat += 1
    else:
        kor += 1

print("Találatok száma: ",talalat)