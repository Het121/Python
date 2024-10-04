# # # # # # # # # # # print("hello Python")
# # # # # # # # # # # Airth

# # # # # # # # # # # a=int(input("Enter Number A"))
# # # # # # # # # # # b=int(input("Entar number B"))

# # # # # # # # # # # print(a+b)
# # # # # # # # # # # print(a-b)
# # # # # # # # # # # print(a*b)
# # # # # # # # # # # print(a/b)
# # # # # # # # # # # print(a%b)


# # # # # # # # # # #Area
# # # # # # # # # # b=int(input("Enter Number b"))
# # # # # # # # # # h=int(input("Enter Number h"))

# # # # # # # # # # print((b*h)/2)


# # # # # # # # # #swap
# # # # # # # # # x=int(input("Enter x"))
# # # # # # # # # y=int(input("Enter y"))
# # # # # # # # # x=x+y
# # # # # # # # # y=x-y
# # # # # # # # # x=x-y
# # # # # # # # # print("x:",x,"Y:",y)

# # # # # # # # #c to f
# # # # # # # # Fahernhit=int(input("Enter Fahernhit"))
# # # # # # # # Celsius=((Fahernhit-32)*5/9)
# # # # # # # # print(Celsius)

# # # # # # # #Positive or Negative
# # # # # # # a=int(input("Enter number A"))
# # # # # # # if (a>0):
# # # # # # #     print("Positive")
# # # # # # # elif(a<0):
# # # # # # #     print("Negative")
# # # # # # # else:
# # # # # # #     print("Zero")
# # # # # # # oddf-even
# # # # # # a=int(input("Enter number A"))
# # # # # # if(a%2==0):
# # # # # #     print("A is Even")
# # # # # # else:
# # # # # #     print("A is Odd")
# # # # # # Prime Number
# # # # # a=int(input("Enter Number"))
# # # # # if a>1:
# # # # #     for i in range(2,int(a/2)+1):
# # # # #         if (a%i==0):
# # # # #             print(a,"not prime")
# # # # #             break
# # # # #         else:
# # # # #             print(a,"Prime")
# # # # #             break
# # # # # else:
# # # # #     print(a,"not prime")
# # # # #  Fact
# # # # a=int(input("Enter Number a"))
# # # # fact=1
# # # # for i in range(1,a+1):
# # # #     fact=fact*i
# # # # print("factorial of",a,"is:",fact)
# # # # multiplication tabale
# # # number=int(input("Enter Number"))
# # # print("Multiplication tabale of",number)
# # # for multipler in range(1,11):
# # #     product=number*multipler
# # #     print(number,"X",multipler,"=",product)
# # # Sum of Natural number
# # def sum_of_num(n):
# #     sum=0
# #     for i in range(1,n+1):
# #         sum += i

# #     return sum
# # n = int(input("Enter")) 
# # print("sum of first",n,"Natural number:",sum_of_num(n))
# # cale
# import calendar
# yy=int(input("Enter Year"))
# mm=int(input("Enter month"))
# print(calendar.month(yy,mm))
# SC

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
select=int(input("Choice 1,2,3,4:"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if select == 1:
    print(num1, "+", num2, "=",
                    add(num1, num2))
 
elif select == 2:
    print(num1, "-", num2, "=",
                    sub(num1, num2))
 
elif select == 3:
    print(num1, "*", num2, "=",
                    mul(num1, num2))
 
elif select == 4:
    print(num1, "/", num2, "=",
                    div(num1, num2))
else:
    print("Invalid input")