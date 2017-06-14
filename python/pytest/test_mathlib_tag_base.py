import mathlib
import pytest
import sys


#This is the tag the test
#"pytest -m windows" This command will run test that is tagged with windows

@pytest.mark.windows
def test_windows_1():
  assert True

@pytest.mark.windows
def test_windows_2():
  assert True

@pytest.mark.mac
def test_mac_1():
  assert True

@pytest.mark.mac
def test_mac_2():
  assert True
