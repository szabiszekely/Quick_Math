import operator
import random

#define operators you wanna use


#sample variables
a = random.randint(1,10)
b = random.randint(1,10)
print(a)
print(b)
lista = ["+","-","*","/"]
string_op = random.choice(lista)
print(string_op)

def operator_hordo(a,b,op):

    allowed_operators={
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}
    
    #sample calculation => a+b
    result = allowed_operators[op](a,b)
    print(result)
    return result

result = operator_hordo(a,b,string_op)
muvelet = int(input(f"{a} {string_op} {b} = "))

if result == muvelet:
    print("Szép munka")
else:
    print("Rossz")
