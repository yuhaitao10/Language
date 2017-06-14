#!/usr/bin/python
def decorator_function(original_function):
  def wrapper_function(*args,**kwargs):
    print('Wrapper executed this before {}'.format(original_function.__name__))
    #return original_function()
    original_function(*args,**kwargs)
  return wrapper_function

#def display():
#  print('display function ran')
#decorated_func = decorator_function(display)
#decorated_func()


#The below function is used to replace the above commented one
@decorator_function
def display():
  print('display function ran')


@decorator_function
def display_info(name, age):
  print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)
display()

