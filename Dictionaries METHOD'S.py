# #DEFINATION:= UNORDER SET KEY:VALUES FORM
# # SYTAX :- {}

# #CREATE Dictionarie

the_dict ={'name' : 'het',
           'age'  : 29,
           'city' : 'pune'    }

print(the_dict)


# #  key Access the Dictionarie using get method in key 



# #you can choose any keyword i am choose x you can use x,y,a.b you're choice ok!
# #you can use get method so show the out put his value

# # let show the example i got a new phone and next day you have buy a new phone it's called get method😊
x = the_dict.get("age")
print(x)
# #when you can use key
y = the_dict.keys()
# #here your qustion why i am write keys() ?? why i am not write key()
# #ans :-  because in the Dicitonaries one or one more than key so we can't ,,  write key we write keys
print(y)


# # value Access  the Dictionarie 

z=the_dict.values()
print(z)

#you can also use two key word key and value in one line
a = the_dict.keys() , the_dict.values()
print(a)


                                                    #modify the dictionary

the_dict["age"] = 30
print(the_dict)

