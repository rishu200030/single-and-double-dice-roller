import random
print("Welcome to dice roller")
print("How many dice do you want to roll")
x=int(input(print("press '1' for an single die and '2' for Double dice")))

def dieroller():
    return random.randint(1,6)


def single_die():
    flag = 1
    while flag ==1 :
        s = int(input(print("to roll a die press '1' and press '0' to exit")))
        if s != 1 :
            return 0
        else :

            print("-----------------------------------------------")
            print(die)
            print("-----------------------------------------------")


def Double_die():
    flag = 1
    while flag ==1 :
        s = int(input(print("to roll a die press '1' and press '0' to exit")))
        if s != 1 :
            return 0
        else :

            a = dieroller()
            b = dieroller()
            print("-----------------------------------------------")
            print(a)
            print(b)
            c = str(a+b)
            print("total sum = "+ c )
            print("-----------------------------------------------")


if x== 1:
    single_die()
elif x==2 :
    Double_die()
else:
    print("please select an valid option")


