def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "Cant'Divided by Zero..."
    else:
        return x / y
print("Select One operation:")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

while True:
    choice=input("Enter Choice(1/2/3/4):")
    if choice in ('1','2','3','4'):
        n1=int(input("Enter Number1:"))
        n2=int(input("Enter Number2:"))

        if choice=='1':
            print(add(n1,n2))
        elif choice=='2':
            print(sub(n1,n2))
        elif choice=='3':
            print(mul(n1,n2))
        elif choice=='4':
            print(div(n1,n2))
    else:
        print("Invalid  choice")