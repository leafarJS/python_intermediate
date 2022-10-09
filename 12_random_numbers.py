import random as rd

a = rd.random()
print(a)

a = rd.uniform(1,10)
print(a)

a = rd.randint(1,10)
print(a)

a = rd.randrange(1,10)# not include 10
print(a)

a = rd.normalvariate(0, 1) #distnorm mu sigma 
print(a)

mylist = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a = rd.choice(mylist)
print(a)

a = rd.sample(mylist, 3)
print(a)

a = rd.choices(mylist, k=4)
print(a)

mylist = list("ABCDEFGHIJKLMNO")
rd.shuffle(mylist)
print(mylist)




rd.seed(1)
print(rd.random())
print(rd.randint(1,100))

rd.seed(2)
print(rd.random())
print(rd.randint(1,100))


rd.seed(1)
print(rd.random())
print(rd.randint(1,100))

rd.seed(2)
print(rd.random())
print(rd.randint(1,100))

import secrets

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
#1010
print(a)

mylist = list("ABCDEFG")
a = secrets.choice(mylist)
print(a)