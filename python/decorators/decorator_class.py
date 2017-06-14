#!/usr/bin/python
class decorator_class(original_function):
  def __init__(self,original_function):
    self.original_function = original_function

  def __call__(self,*args,**kwargs):
    print('call method executed this before {}'.format(self.original_function.__name__))
    return self.original_function(*argv,**kwargs)

@decorator_class
def display():
  print('display function ran')


@decorator_class
def display_info(name, age):
  print('display_info ran with arguments ({}, {})'.format(name,age))

display_info('John', 25)
display()

