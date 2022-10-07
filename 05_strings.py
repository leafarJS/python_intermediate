#string ordered, inmutable, text representation
my_str = "hello world!"
print(my_str)

my_str = "hello\nworld!"
print(my_str)

my_str = """
multiple lines
"""
print(my_str)

my_str = "hello\nworld!"
char = my_str[0]
print(char)
char = my_str[-1]
print(char)

my_str = "hello\nworld!"
#my_str[0] = "H" #error
print(my_str)

#TODO: aplica como en tupla desde la linea 34
sub_str = my_str[2:5]
print(sub_str)

sub_str = my_str[::-1] #reverse string
print(sub_str)

a = "hello"
b = "world"
sentence = a + " " + b
print(sentence)
print(f"{a} {b}")

for i in sentence:
  print(i)
  
if "l" in sentence:
  print("Yes")
else:
  print("Not found!")

my_str = "          hello world     "
print(my_str)
my_str = my_str.strip()
print(my_str)


print(my_str.upper())
print(my_str.lower())
print(my_str.startswith("h"))
print(my_str.startswith("hello"))
print(my_str.endswith("d"))
print(my_str.endswith("world"))
print(my_str.find("o"))
print(my_str.find("hello"))
print(my_str.count("o"))
print(my_str.count("z")) #0
print(my_str.replace("world", "universe"))
print(my_str.replace("worldddd", "universe")) # string original
my_str = 'how are you doing'
my_list = my_str.split()
print(my_list)

my_str = 'how are, you doing'
my_list = my_str.split(',')
print(my_list)

my_str = 'how | are you doing'
my_list = my_str.split('|')
print(my_list)



my_str = 'how are you doing'
my_list = my_str.split()
print(my_list)
new_str = ''.join(my_list)
print(new_str)


my_str = 'how are you doing'
my_list = my_str.split()
print(my_list)
new_str = ' '.join(my_list)
print(new_str)


print("=*" * 10) 

from timeit import default_timer as timer

my_list = ["a"] * 6000000
#print(my_list)

start = timer()
my_str = ''
for i in my_list:
  my_str += i
#print(my_str)
stop = timer()

print(stop - start)
print("=*" * 10) 
start = timer()
my_str = ''.join(my_list) #more effective
#print(my_str)
stop = timer()

print(stop - start)
print("=*" * 10) 


#%, .format(), f-String
var = "TOM"
str = "Sit eos nonumy nonumy gubergren dolore stet sanctus. No amet eirmod consetetur ut sea sit. Accusam magna et magna vero.%s" % var

print(str)

var = 100000
str = "Sit eos nonumy nonumy gubergren dolore stet sanctus. No amet eirmod consetetur ut sea sit. Accusam magna et magna vero.%d" % var

print(str)

var = 100000.35
str = "Sit eos nonumy nonumy gubergren dolore stet sanctus. No amet eirmod consetetur ut sea sit. Accusam magna et magna vero.%2f" % var

print(str)


var = "LOREM"
str = "Sit eos nonumy nonumy gubergren dolore stet sanctus. No amet eirmod consetetur ut sea sit. Accusam magna et magna vero.{}".format(var)

print(str)

var = 3.14169
var2 = 3.144444
str = "Sit eos nonumy nonumy gubergren dolore stet sanctus. No amet eirmod consetetur ut sea sit. Accusam magna et magna vero.{:.2f} and {}".format(var, var2)

print(str)

var = "CAMINAR"
var2 = 13251
str = f"Sit eos nonumy nonumy gubergren dolore stet sanctus.{var} No amet eirmod consetetur ut sea sit. Accusam {var2 * 1000} magna et magna {var2} vero."

print(str)