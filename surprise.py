def pattern():
    for i in range(len(name)):
        #for A
        if name[i] == "a" or "A":
            print_A = [[" " for i in range (6)]for j in range(7) ]
            for row in range (7):
                for col in range(6):
                    if((col==0 or col==5) and row!=0) or row==3 or (row==0 and (col!=0 and col!=5)):
                        print_A[row][col] = "♥"
            list2.append(print_A)
        # for B
        elif name[i]=="B" or "b":
            print_B = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_B[row][col] = "♥"
            list2.append(print_B)
        #for c
        elif name[i]=="C" or "c":
            print_C = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_C[row][col] = "♥"
            list2.append(print_C)
        #for D
        elif name[i]=="D" or "d":
            print_D = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_D[row][col] = "♥"
            list2.append(print_D)
        #for E
        elif name[i]=="E" or "e":
            print_D = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_D[row][col] = "♥"
            list2.append(print_D)
        #for F
        elif name[i]=="F" or "f":
            print_F = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_C[row][col] = "♥"
            list2.append(print_F)
        #for G
        elif name[i]=="G" or "g":
            print_G = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_G[row][col] = "♥"
            list2.append(print_G)
        #for H
        elif name[i]=="H" or "h":
            print_H = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_H[row][col] = "♥"
            list2.append(print_H)
        #for I
        elif name[i]=="I" or "i":
            print_I = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_I[row][col] = "♥"
            list2.append(print_I)
        #for J
        elif name[i]=="J" or "j":
            print_J = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_J[row][col] = "♥"
            list2.append(print_J)
        #for k
        elif name[i]=="k" or "K":
            print_K = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_K[row][col] = "♥"
            list2.append(print_K)
        #for L
        elif name[i]=="L" or "l":
            print_L = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_L[row][col] = "♥"
            list2.append(print_L)
        #for m
        elif name[i]=="m" or "M":
            print_M = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_M[row][col] = "♥"
            list2.append(print_M)
        #for n
        elif name[i]=="N" or "n":
            print_N = [[" " for i in range(6)] for j in range(7)]
            for row in range(7):
                for col in range(6):
                    if
                        print_N[row][col] = "♥"
            list2.append(print_N)












if __name__ == '__main__':

    name = input("enter the name: ")
    list2 = []
    list3 = pattern()
    for i in range(7):
        for j in range (len(list3)):
            for k  in range (6):
                print (list3[j][i][k],end = " ")
            print(end= " ")
        print()