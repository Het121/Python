a=input("enter somthing:")
w=a.split()
for i in range(len(w)):
    w[i]=w[i].lower()
w.sort()
print(w)