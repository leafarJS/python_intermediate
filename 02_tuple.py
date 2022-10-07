mytuple = ("max", 28, "min")
print(mytuple)

mytuple = tuple(["max", 28, "min"]) #se la puede volver iterable si esta por dentro como un array

print(mytuple[0])
print(mytuple[1])
print(mytuple[2])
print(mytuple[-1])
print(mytuple[-2])
print(mytuple[-3])

for i in mytuple:
  print(i)
  
if "max" in mytuple:
  print("Yes")
else:
  print("No")
  
my_tuple = {"a", "b", "c", "d", "e", "f"}
print(my_tuple)
print(len(my_tuple))
#print(my_tuple.count("a")) #no se puede utilizar
#print(my_tuple.index("c")) #no se puede utilizar
  
mylist = list(my_tuple)

print(mylist.count("a")) 
print(mylist.index("c")) 
  
a = (1,2,3,4,5,6,7,8,9,10) #con {} no funciona

print("=|" * 20)
b = a[2:5]
print(b)
c = a[2:]
print(c)
d = a[:5]
print(d)
e = a[::2]
print(e)
f = a[2::]
print(f)
g = a[1::3]
print(g)
print("=|" * 20)  


my_tuple = "max", 45, "min" #se puede pero no recomendable
maximo, year, minimo = my_tuple
print(maximo, year, minimo)


mytuple_num = [0,1,2,3,4,5]

a, *b, c = mytuple_num
print("=/" * 10) 
print(a)
print(b)
print(c)
print("=/" * 10) 

import sys
mylist = [0,1,2,"hello", True]
mytuple = (0,1,2,"hello", True)
print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")
print("=/" * 10) 

import timeit
print(timeit.timeit(stmt="[1,2,3,4,5,6]", number=1000000)) #not efficient
print(timeit.timeit(stmt="(1,2,3,4,5,6)", number=1000000)) #more efficient
print("=/" * 10) 


  
  
  
  
  
  
  
  