number=int(input("Enter Number:"))
print("Multiplication Table of",number)
for multipler in range(1,11):
    product = number * multipler
    print(number,"X",multipler,"=",product)