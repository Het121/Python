def sum_natural(n):
    sum=0
    for i in range(1,n + 1):
        sum+=i
    return sum
number=int(input("Enter number:"))
result=sum_natural(number)
print("The Sum of Natural Numbers up to",number,"is",result)