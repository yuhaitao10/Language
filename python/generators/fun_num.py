#!/usr/bin/python

def square_numbers(num_list):
  result = []
  for i in num_list:
    result.append(i*i)
  return result

#squares = square_numbers([1,2,3,4,5,6])
squares = [x*x for x in [1,2,3,4,5,6]]
print(squares)
