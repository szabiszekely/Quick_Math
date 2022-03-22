import operator
import random


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

print(op_hordo_10_15())
print(f"{a} {string_op_1} {b} {string_op_2} {c} = ")