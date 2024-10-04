def convert(list1):
    dict={

    }
    for i in range(0,len(list1),2):
        dict[list1[i]]=list1[i+1]
    return dict
l1=['a',1,'b',2,'c',3]
print(convert(l1))
