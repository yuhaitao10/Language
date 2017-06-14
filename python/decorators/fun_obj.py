#!/usr/bin/python

def outer1_function():
  message = 'Hi'

  def inner1_function():
    print(message)
  return inner1_function()

#The function is called automatically
outer1_function()


def outer2_function():
  message = 'Hello'

  def inner2_function():
    print(message)
  return inner2_function

ff = outer2_function()
#need to call this funtion
ff()
ff()
ff()

def outer3_function(msg):
  def inner3_function():
    print(msg)
  return inner3_function

hi_func = outer3_function('Hi')
bye_func = outer3_function('Bye')

hi_func()
bye_func()
