# # # # # def factg(n):
# # # # #  if n==0:
# # # # #   return 1
# # # # #  else:
# # # # #   return n*factg(n-1)
# # # # # number = int(input("enter number"))
# # # # # print("factorial of",number,"is:",factg(number))
# # # # # string
# # # # str="hello world"
# # # # print(str.upper())
# # # # print(str.lower())
# # # # print(str.count("hello"))
# # # # print(str.split())
# # # # print(str.replace("world","Python"))
# # # # # print(str.[6:12])
# # # # sort
# # # my_str="this is a python programinng language"
# # # words=[word.lower() for word in my_str.split()]
# # # words.sort()
# # # print("word sorted:")
# # # for word in words:
# # #     print(word)
# # # punct
# # punct="!()-[],$,@"
# # my_str="Hello !! I--am"
# # no_punct=""
# # for char in my_str:
# #     if char not in punct:
# #         no_punct=no_punct+char
# # print(no_punct)
# # rev str
# str="Hello World"
# print(str[::-1])
# list to str
# list1=["Apple","Banana"]
# str1="".join(list1)
# print(type(str1))
# int to str
# num=10
# str_num=str(num)
# print(type(str_num))
# con str
# str1="hello "
# str2="world!"
# str3=str1+str2
# print(str3)
# append
# fruits=["apple","banana"]
# fruits.append("grapes")
# print(fruits)
# campare
# list1=["apple","banana"]
# list2=["apple","banana"]
# if list1==list2:
#     print("Equal")
# else:
#     print("not")
# con lis to dict
# my=[('a',1),('b',2),('c',3)]
# my_dict=dict(my)
# print(my_dict)
# # remove
# list1=[1,2,3,4,6,48,6]
# print("before removing eledment",list1)
# list1.remove(2)
# print("after removing eledment",list1)
# # add list
# list1=[1,2,3,4,5,6,7]
# list2=[8,9,10,11,12,13,14]
# print(list1+list2)
# cin list to string
# def list_to_str(l):
#     str=""
#     for char in l:
#         str += char+" "
#     return str
# list1=["apple","banana"]
# print(list_to_str(list1))
# # cr dict
# dict={
#     "name":"Jhon",
#     "email":"sk@gmail.com",
#     "class":"E",
#     "age":45,
# }
# print(dict)
# # convert list to dict
# def  convert(list1):
#     s=""
#     dict={}
#     for i in range(0,len(list1),2):
#         dict[s+[i]]=s+[i+1]
#     return dict
# list1=[('a,1'),('b',2),('c,',3)]
# print(convert(list1))
# merage dic
# def dictionary(dict1,dict2):
#     # dictionary=dict.copy()
#     # dictionary=update(dict2)
#     return dictionary
# dict1={
#      "name":"Jhon",
#      "email":"sk@gmail.com",
#      "class":"E",
#      "age":"45",
#  }
# dict2={"city":"USA"}
# dictionary1=dictionary(dict1+dict2)
# print(dictionary1)
# # sort
# my_dict={'shubham':10,'jhon':45,'thala':42}
# myKeys=list(my_dict.keys())
# myKeys.sort()
# sorted_dict={i:my_dict[i]for i in myKeys}
# print(sorted_dict)
# merge
# Python code to merge dict using update() method
# def Merge(dict1, dict2):
# 	return(dict2.update(dict1))


# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}

# print(Merge(dict1, dict2))

# print(dict2)
# instance
class fruit:
    def __init__(self,name,color,taste):
        self.name=name
        self.color=color
        self.taste=taste
        apple=fruit(apple,"red,sweet")
        banana=fruit(banana,"yellow,sweet")
        chiku=fruit(chiku,"brown,sweet")
    print(apple.name)
    print(banana.color)
    print(chiku.taste)

