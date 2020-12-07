# Health Management System
'''1-Total 6 Files, 3 For exercise and 3 For for diet
2-3 clients - Harry, Rohan and Hammad
3-write a function that when executed takes as input client name
4-one more function to retrieve exercise or food for any client'''

import datetime

def getdata():
    return datetime.datetime.now()
def take(b):
    if b==1:
        c=int(input("enter 1 for exercise 2 for food: "))
        if c==1:
            value=input("type here: ")
            with open("harryEX.txt","a") as he:
                he.write(str([str(getdata())])+":"+str({value})) #try karna hai ki yaha agar input pehle likhte aaur value nahi likhte to kya hota?
                print("done writing")
        elif c==2:
            value=input("type here: ")
            with open("harryfood.txt","a") as he:
                he.write(str(getdata())+":"+value)
                print("we got your food")
        else:
            print("please enter only given key")

    elif b==2:
        c=int(input("enter 1 for exercise and 2 for for food: "))
        if c==1:
            value=input("type here: ")
            with open("rohanEX.txt","a")as ro:
                ro.write(str(getdata())+":"+value)
        elif c==2:
            value=input("type here: ")
            with open("rohanfood.txt","a") as ha:
                ha.write(str(getdata())+":"+value)
                print("we got your food")
        else:
            print("please enter only given key")
    elif b==3:
        c = int(input("enter 1 for exercise and 2 for for food: "))
        if c==1:
            value = (input("type here: "))
            with open("harishEX.txt","a") as hr:
                hr.write(str(getdata()) + ":" + value, "a")
                print("done writing")
        elif c==2:
            value = (input("type here: "))
            with open("harishfood.txt","a") as hr:
                hr.write(str(getdata()) + ":" + value)
                print("we got your food")
        else:
            print("please put only given number: ")
def release(d):
    if d==1:
        c = int(input("enter 1 for exercise 2 for food: "))
        if c==1:
            with open("harryEX.txt","r") as har:
                for i in har:
                    print(i,end='')
        elif c==2:
            with open("harryfood.txt","r") as hf:
                for i in hf:
                    print(i, end='')
    elif d==2:
        c = int(input("enter 1 for exercise 2 for food: "))
        if c == 1:
            with open("rohanEX.txt","r") as rh:
                for i in rh:
                    print(i, end='')
        elif c==2:
            with open("rohanfood.txt","r") as rf:
                for i in rf:
                    print(i,end='')
    elif d==3:
        c = int(input("enter 1 for exercise 2 for food: "))
        if c == 1:
            with open("harishEX.txt","r") as he:
                for i in he:
                    print(i,end='')
        elif c==2:
            with open("harishfood.txt","r") as hf:
               for i in hf:
                   print(i,end='')
    else:
        print("please enter given keyword only")



if __name__ == '__main__':

     n=1;q=1
     while n==1:
        print("health mangement")
        i=int(input("enter 1 to lock value or 0 for retrieve: "))
        if i==1:
            lock=int(input("enter 1 for harry \nenter 2 for rohan\nenter 3 for harish: \n"))
            take(lock)
        else:
            retrive=int(input("enter 1 for harry \nenter 2 for rohan\nenter 3 for harish: \n"))
            release(retrive)
            print("\n")
        n = ord(str(input("enter q to quite the program and c to continue the program: ")))
        if n == 113 or n == 81:
            quit()
        elif n == 67:
            n=n - 66
        elif n == 99:
            n=n - 98











