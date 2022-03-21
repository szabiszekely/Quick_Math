import random

def jelöltek():
    global szotar
    szotar = {}

    lista = ['+','-']
    random_1 = random.randint(1,10)
    random_2 = random.randint(1,10)
    random_osszjel = random.choice(lista)
    szotar.update({"szam_1":random_1})
    szotar.update({"szam_2":random_2})
    szotar.update({"matekjel":random_osszjel})
    print(szotar)

    ossz = ("{:02d} {} {:02d}").format(random_1,random_osszjel,random_2)
    print(ossz)
    print(random_1,random_osszjel,random_2)
jelöltek()



















