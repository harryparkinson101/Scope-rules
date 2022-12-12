a = 1

def parent():
  def confusion():
    return sum
  return confusion()

print(parent())
print(a)

# Start with local
# Parent Global
# global
# built in python functions

total = 0

def count():
  #total is not defined within the fuction so the word global will find the value fo total from global scope
  global total
  
  total += 1
  return total
count()
count()
print(count())

# Dependency Injection

def counting(total):
  total += 1
  return total

print(counting(counting(counting(total))))