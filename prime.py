num=int(input("Enter number:"))
if num > 1:
    for i in range(2,int(num/2)+1):
        if(num%i)==0:
            print(num,"is Not prime Number")
            break
    else:
            print(num,"is prime number")
else:
    print(num,"is not a prime number")