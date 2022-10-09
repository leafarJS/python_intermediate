def start_and_decorator(func):
  
  def wrapper():
    print('start')
    func()
    print('end')
  return wrapper

@start_and_decorator
def print_name():
  print('Jorge')

print_name = start_and_decorator(print_name)
print(print_name())




import functools
def start_end_decorator_1(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_1
def add_5(x):
    return x + 5
result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)



def my_decorator(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    #do...
    result = func(*args, **kwargs)
    #do...
    return result
  return wrapper

@my_decorator
def add_6(x):
    return x + 5
result = add_6(20)
print(result)
print(add_6.__name__)
help(add_6)




def repeat(num_items):
  def decorator_repeat(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_items):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_items = 10)
def greet(name):
  print(f"hello, welcome {name}")


greet("Jorge Rafael")



def start_end_decorator_8(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

@debug
@start_end_decorator_8
def say_hello(name):
  greeting = f"Hello mather fucker {name}"
  print(greeting)
  return greeting

say_hello("Rafael Jorge")

class CountCalls:
  def __init__(self, func):
    self.func = func
    self.num_calls = 0
    
  def __call__(self,*args, **kwargs):
    self.num_calls += 1
    print(f"this is executed {self.num_calls} times")
    return self.func(*args, **kwargs)
  
#cc = CountCalls(None)
#cc()


@CountCalls
def saludar():
  print("hola!!!")
  
  
saludar()
saludar()
saludar()