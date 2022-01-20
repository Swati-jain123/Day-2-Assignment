num=3; #integer
age=4;
print(num,age)
print("num is {} and age is {}".format(num,age))
print(f"num is {num} and age is {age}")
print("num is %d and age is %d"%(num,age))
a=1.679 #float
b=567.979
print(a,b)
print("a is {} and b is {}".format(a,b))
print("a is %f and b is %f"%(a,b))
print(f"a is {a} and b is {b}")
i=True #boolean
j=False
print(i,j)
type(i)
print("i is %s and j is %s"%(i,j))  
print("i is {} and j is{} ".format(i,j))
print(f"i is {i} and j is {j}")
#list
names=["swati","mansi","princy","priyanshi","krati"]
marks=[56,89,78,9,56,43]
print(names,marks)
print("name of students : {} and marks :{}".format(names,marks))
print("name : %s and marks:%s "%(names,marks))
print(f"names : {names} and marks : {marks}")
#tuple

a=tuple()
a=(67,78,85)
b=(78,89,696969,79)
print(a,b)
print("a : {} and b :{}".format(a,b))
print(f"a : {a} and b:{b}")
#dict
info=dict()
info={}
info['name']='lets upgrade'
info['age']=34
print(info)
print("information is {}".format(info))
print("information is %s"%(info))
print(f"information is {info}")
#set
items=set()
items=1,4,7,95,4,33,89,9
print(items)
print("items are {}".format(items))
print(f"items are : {items}")