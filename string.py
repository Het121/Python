#
# #COnvert the string to uppeer  case
# str =  input("enter the string")
# print(str.upper())
#
# #COnvert the string to lower  case
# str =  input("enter the string")
# print(str.lower())
#
# # #Check the string this  is lower case yes or no
# str_input = input("Enter the string: ")
# c, o = 0, 0
# for i in str_input:
#     if i.isupper():
#         c += 1
#     else:
#         o += 1
# print("Number of uppercase characters:", c)
# print("Number of lowercase characters:", o)

#swape case  :- mens lower case to convert upper case and upper case to lower case && alos we can use capitalize

str_input = input("enter the string")
#you can choose any variable i am choose c
c = str_input.swapcase()
d = str_input.capitalize()
print(c)
print(d)


