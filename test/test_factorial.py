import pytest
from src.factorial import *

def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_typeError():
    with pytest.raises(TypeError):
        factorial("r") == 0

def test_factorial_valueError():
   with pytest.raises(ValueError):
     factorial(-5) == -5

def test_factorial_5():
    assert factorial(5) == 120