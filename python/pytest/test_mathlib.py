import mathlib
import pytest
import sys


#skip this test
@pytest.mark.skip(reason="I dont want to run this test now")
def test_calc_sum():
  total = mathlib.calc_sum(4,5)
  assert total == 9

def test_calc_multiply():
  result = mathlib.calc_multiply(10,3)
  assert result == 30

#conditional skip this test based a condition
@pytest.mark.skipif(sys.version_info > (1,3), reason="I dont want to run this test now")
def test_calc_total():
  total = mathlib.calc_total(5,6)
  assert total == 11

#dummy test case
def test_dummy():
  assert True

#parameterized test that mathlib.calc() is tested with multiple different parameters
@pytest.mark.parametrize("test_input, expected_output",
                         [
                           (5,25),
                           (9,81),
                           (10,100) 
                         ]
                        ) 

def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output 
