#!/usr/env/bin python
from complex import Complex
from math import sqrt

def test_add_one():                 #first unit test for addition of two complex numbers
    x = Complex(10,2)               #complex number 1
    y = Complex(5,3)                #complex number 2
    z = x + y                       #Adding two complex numbers, z is complex number 3
    assert z == Complex(15,5)       #z should be equal to Complex(15,5) i.e., 15+5i

def test_add_two():                 #second unit test for addition of two complex numbers
    x = Complex(3,2)                
    y = Complex(1,0)                
    z = x + y                       
    assert z == Complex(4,2)

def test_add_three():
    x = Complex(0,2)
    y = Complex(4,1)
    z = x + y
    assert z == Complex(4,3)

def test_sub_one():                 #unit tests for checking subtraction of two complex numbers
    x = Complex(10,8)
    y = Complex(6,3)
    z = x - y
    assert z == Complex(4,5)

def test_sub_two():
    x = Complex(1,3)
    y = Complex(0,2)
    z = x - y
    assert z == Complex(1,1)

def test_sub_three():
    x = Complex(0,3)
    y = Complex(2,3)
    z = x - y
    assert z == Complex(-2,0)

def test_sub_four():
    x = Complex(10,2)
    y = Complex(2,0)
    z = x - y
    assert z == Complex(8,2)

def test_mul_one():                  #first unit test for multiplication of two complex numbers
    x = Complex(1,4)
    y = Complex(5,1)
    z = x * y
    assert z == Complex(1,21)

def test_mul_two():
    x = Complex(1,2)
    y = Complex(3,0)
    z = x * y
    assert z == Complex(3,6)

def test_mul_three():
    x = Complex(0,1)
    y = Complex(7,3)
    z = x * y
    assert z == Complex(-3,7)

def test_mod_one():                     #unit tests for modulus of a complex number
    x = Complex(6,-8)
    assert x.modulus() == sqrt(100)

def test_mod_two():
    x = Complex(-5,4)
    assert x.modulus() == sqrt(41)

def test_mod_three():
    x = Complex(6,0)
    assert x.modulus() == sqrt(36)

def test_mod_four():
    x = Complex(0,8)
    assert x.modulus() == sqrt(64)

def test_conjugate_one():               #first unit test for conjugate of complex number
    x = Complex(4,5)
    assert x.conjugate() == '4-5i'

def test_conjugate_two():
    x = Complex(4,3)
    assert x.conjugate() == '4-3i'

def test_conjugate_three():
    x = Complex(0,5)
    assert x.conjugate() == '0-5i'

def test_equal_one():                   #unit test for checking if two complex numbers are equal
    x = Complex(2,4)
    y = Complex(4,2)
    assert x.__eq__(y) == False

def test_equal_two():
    x = Complex(2,4)
    y = Complex(2,4)
    assert x.__eq__(y) == True

def test_equal_three():
    x = Complex(-2,4)
    y = Complex(4,-2)
    assert x.__eq__(y) == False

def test_equal_four():
    x = Complex(2,-4)
    y = Complex(2,-4)
    assert x.__eq__(y) == True

def test_radd():                    #test for checking custom Complex and Python complex numbers addition
    x = Complex(2,3) 
    y = (2+2j) 
    z = y + x
    assert z == Complex(4,5)

def test_rsub():
    x = Complex(2,3)
    y = (2+2j)
    z = x - y
    assert z == Complex(0,1)

def test_rmul():
    x = Complex(3,3)
    y = (4+2j)
    z = x * y
    assert z == Complex(6,18)

def test_real_complex_combined_one():           #test for real and Complex number add, sub and mul
    assert (4*Complex(3,4)-2) == Complex(10,16)

def test_real_complex_combined_two():
    assert (3+Complex(3,4)-2) == Complex(4,4)

def test_real_complex_combined_three():
    assert (10-Complex(3,4)+5) == Complex(-2,4)