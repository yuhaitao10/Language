import mathlib
import pytest
import sys


def test_calc_sum():
  total = mathlib.calc_sum(4,5)
  assert total == 9


#pytest -k multiply
#This command will only run test with names that has multiply
def test_calc_multiply():
  result = mathlib.calc_multiply(10,3)
  assert result == 30

def test_calc_total():
  total = mathlib.calc_total(3,5)
  assert total == 8
