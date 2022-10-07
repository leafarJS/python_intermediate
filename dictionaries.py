#key value pairs mutable
mydict = {
  "name":"max",
  "age":45,
  "city":"bolivia"
}
print(mydict)


mydict2 = dict(name="min", age=54, city="Canada")
print(mydict2)

value = mydict["age"]
print(value)

mydict["email"] ="zzz@gmail.com" 
print(mydict)

mydict["email"] ="cambiomail@gmail.com" 
print(mydict)

del mydict["email"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

if "name" in mydict:
  print(mydict["name"])
else:
  print("Not found!")
  
mydict["age"]=45
mydict["number"] = 76797502

try:
  print(mydict["names"])
except:
  print("Error Not found!")
  
for key in mydict.keys():
  print(key)  

for value in mydict.values():
  print(value)
  
for key, value in mydict.items():
  print(key, value)
  
mydict_copy = mydict # acepta cambios en el original
#TODO: options 
#mydict_copy = dict(mydict) # no es igual al original si se adiere otro elemento
#mydict_copy = mydict.copy() # no es igual al original si se adiere otro elemento

print(mydict_copy)
mydict_copy["email"] = "xxx@gmail"
print(mydict)
print(mydict_copy)

print("=/" * 10) 
mydict = {
  "name":"max",
  "age":45,
  "email":"xxx@gmail.com",
}
mydict2 = dict(name="min", age=54, city="Canada")

mydict.update(mydict2)
print(mydict)
print("=/" * 10) 

my_dict ={3:9, 6:36, 9:81}
print(my_dict)

#mytuple = [8,7]
#mytuple = (8,7)
#my_dict = {mytuple:15}

print("=/" * 10) 