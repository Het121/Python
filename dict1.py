my_dict={'shubham':10,'jhon':45,'thala':42}
mykeys=list(my_dict.keys())
mykeys.sort()
sorted_dict={i:my_dict[i] for i in mykeys}
print(sorted_dict)