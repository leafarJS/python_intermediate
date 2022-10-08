#errors and exceptions
try:
  a = 5 / 0
except:
  print('an error happened')
  
try:
  a = 5 / 0
except Exception as e:
  print(e)

try:
  a = 5 / 0
  b = a + 4
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print('everything is fine')
finally:
  print('cleaning up...')


class ValueTooHighError(Exception):
  pass

class ValuetooSmallError(Exception):
  def __init__(self, msg, value):
    self.msg = msg
    self.value = value
    

def test_value(x):
  if x > 100:
    raise ValueTooHighError('value is too high')
  if x < 5:
    raise ValuetooSmallError('value is too low', x)

try:
  #test_value(200)
  test_value(1)
except ValueTooHighError as e:
  print(e)
except ValuetooSmallError as e:
  print(e.msg, e.value)
  




x = -5
if x < 0:
  raise Exception('x should be positive')

x = 5
if x < 0:
  raise Exception('x should be positive') # sin mensaje

x = -10
assert (x >= 0), 'x is not negative'
