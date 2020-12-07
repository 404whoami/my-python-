import time
import random
def start():
    chance=10
    print("you have 10 chances only")
    user = 0
    comp = 0
    while chance!=0:

        list = ["Stone", "Paper", "scissor"]
        computer = random.choice(list)
        choose = input("choose S for Stone\nchoose P for paper\nchoose C for scissor: ").upper()
        if choose == 'S' and computer == 'Stone':
            print("draw match")
            print(f"computer choosed {computer} and you choosed {choose}")
        elif choose == 'S' and computer == 'Paper':
            print("computer won")
            print(f"computer choosed {computer} and you choosed {choose}")
            comp += 1
        elif choose == 'S' and computer == 'Scissor':
            print(f"computer choosed {computer} and you choosed {choose}")
            print("you won")
            user += 1
        elif choose == 'P' and computer == 'Stone':
            print(f"computer choosed {computer} and you choosed {choose}")
            print('you won')
            user += 1
        elif choose == 'P' and computer == 'Paper':
            print(f"computer choosed {computer} and you choosed {choose}")
            print("draw match")
        elif choose == 'P' and computer == 'Scissor':
            print(f"computer choosed {computer} and you choosed {choose}")
            print("computer won")
            comp += 1
        elif choose == 'C' and computer == 'Stone':
            print(f"computer choosed {computer} and you choosed {choose}")
            print("computer won")
            comp += 1
        elif choose == 'C' and computer == 'Paper':
            print(f"computer choosed {computer} and you choosed {choose}")
            print("you won")
            user += 1
        elif choose == 'C' and computer == 'Scissor':
            print(f"computer choosed {computer} and you choosed {choose}")
            print("draw match")

        chance-=1
        print("*********now you have", chance, "chances********")
    if user>comp:
        print(f"you won the match got {user} points while computer got {comp}")
    elif comp>user:
        print(f"computer won the match got {comp} points while you got {user}")
    else:
        print("both are equal points so draw matches")

if __name__ == '__main__':
    print("WELCOME TO STONE PAPER SCISSOR GAME")
    print("so let's play the game")
    try:
        n = input("enter 1 to start the game and 0 to quite the game: ")
        n=int(n)
        if n==1:
                    start()
        elif n==0:
                    print("THANK YOU")
                    quit()
        else:
                    print("please input a valid key")
    except ValueError or NameError:
             print(f"{n} is not a number")
    time.sleep(20)









