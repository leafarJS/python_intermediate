my_list = ["platano","fresa","pera", "manzana"]

print(my_list)

print(len(my_list))

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

for i in my_list:
  print(my_list)
  
for i in my_list:
  print(i)

if "banana" in my_list:
  print("Yes")
else:
    print("No")

my_list.append("limon")
print(my_list)

my_list.insert(3, "cherrys")
print(len(my_list))

my_list.append(123456)
print(len(my_list))

item = my_list.pop()
print(item)
print(my_list)

item = my_list.remove('pera')
print(my_list)

mylist = [4,3,1,-1,-4,10]

print(mylist)
new_list = sorted(mylist)
print(new_list)

mylist = [0] * 6
print(mylist)

mylist2 = [1,2,3,4,5,6]

new_list = mylist + mylist2 # solo se puede sumar
print(new_list)

mylist = [0,1,2,3,4,5,6,7,8,9]

a = mylist[:]
print(a)

b = mylist[3:]
print(b)

c = mylist[:4]
print(c)

d = mylist[0:7]
print(d)

my_list_org = ["platano","fresa","pera", "manzana"]
list_copy = my_list_org

list_copy.append("limon")

print(list_copy)
print(my_list_org)


x = [1,2,3,4,5,6,7,8,9,10]
y = [i + i for i in x] #elevado al cuadro con loop
print(x)
print(y)










