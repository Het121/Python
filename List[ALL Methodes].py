# WE CREATE A LIST
Thelist = ["A","B","C"]
print(Thelist)

# START THE METHOD'S IN THE LIST

# Access the list
#in the Access list is two way 0 indexing and -1 indexing

Thelist = ["A","B","C"]
print(Thelist[1])
print(Thelist[-1])

# change the list 

Thelist =  ["A","B","C","e","f"]
Thelist[1]="7"
Thelist[0:2]=["10","20"]
print(Thelist)

# add items into the list


Thelist = ["A", "B", "C", "e", "f"]
Thelist.append( "d")
print(Thelist)

# when you have join the two list using .extand keywod in the list

Thelist = ["A", "B", "C", "e", "f"]
Akist= ["jai jai shree gokulesh"]
Thelist.extend(Akist)
print(Thelist)


