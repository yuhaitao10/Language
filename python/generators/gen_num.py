#!/usr/bin/python

def square_numbers(num_list):
  for i in num_list:
    yield (i*i)

#A generate object is created here
squares = square_numbers([1,2,3,4,5,6])

#squares = [ x*x for x in [1,2,3,4,5,6]]

print next(squares)
print next(squares)
print next(squares)
print next(squares)
print next(squares)
print next(squares)
print next(squares)

#print list(squares)

#for i in squares:
#  print i
