import operator
import random







def operator_hordo():
    
    #define operators you wanna use
    allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}
    
    #sample variables
    global a
    a = random.randint(1,10)
    #print(a)
    
    global b
    b = random.randint(1,10)
    #print(b)
    
    lista = ["+","-","*","/"]
    global string_op
    string_op = random.choice(lista)
    #print(string_op)
    
    
    
    #sample calculation => a+b
    result = allowed_operators[string_op](a,b)
    #print(result)
    
    if not result % 1 == 0:
        #print("IGEN")
        while not result % 1 == 0:
            a = random.randint(1,10)
            b = random.randint(1,10)
            #print("-----")
            #print(a)
            #print(b)
            result = allowed_operators[string_op](a,b)
            
            #print(result)
    return result

talalat = 0
kor = 1
while kor <= 10:

    vegeredmeny = operator_hordo()
    print("oOoOoOooOoOoOo")
    print("Kör: ",kor)
    muvelet = int(input(f"{a} {string_op} {b} = "))
    
    if vegeredmeny == muvelet:
        kor += 1
        talalat += 1
    else:
        kor += 1

print("Találatok száma: ",talalat)














