# n=int(input("enter the number: "))
# for i in range(n):
#     print(' '*(n-i-1),end='') #no of spaces in every row:n-i-1
#     for j in range(i+1):#no of symbols in each rows:i+1
#         print(chr(64+n-j),end=' ')#which symbol
#     print()
#
'''3rd one is the symbol generate 2nd times before 1st code apply'''
n=int(input("enter:"))
for i in range(n):
    for j in range (i+1):
       print(chr(65+j),end=' ')
    print()