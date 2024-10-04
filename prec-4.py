#====how to pattern using *(star)

def pattern1(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k  in range(1,1*i):
            print("*",end="")
        print()
pattern1(5)