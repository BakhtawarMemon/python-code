#!/usr/bin/env python
from math import sqrt           #from math module import sqrt function
class Complex:                  
    """This is a custom class of complex numbers

    Attributes:
        r (str): The real part of complex number
        i (str): The imaginary part of complex number
        z (str): String representation of complex number
    """
    def __init__(self, r, i):
        """The constructor for Complex class

        Args:
            r (str): The real part of complex number
            i (str): The imaginary part of complex number
        """
        self.r = r
        self.i = i
        self.z = ""
        if self.r == 0 and self.i == 1:                         #Becasue Complex(0,1) == i 
            self.z = 'i'
        elif self.r == 0:                                       #Because Complex(0,4) == 4i
            self.z = str(self.i) + 'i'
        elif self.i < 0:                                        #Complex(3,-4) == 3-4i
            self.z = str(self.r) + '-' + (str(self.i))[-1] + 'i'
        else:
            self.z = str(self.r) + '+' + str(self.i) + 'i'      #Complex(3,4) == 3+4i
    
    def __str__(self):
        """A function to represent complex number in string format

        Returns:
            str: The string representation of complex number
        """
        return self.z

    def conjugate(self):
        """A function to return conjugate of a complex number

        Returns:
            str: The conjugate of complex number
        """
        self.z = str(self.r) + '-' + str(self.i) + 'i'
        return self.z

    def modulus(self):
        """A function to calculate modulus of a complex number

        Returns:
            float: The modulus of complex number
        """
        t = ((self.r**2)+(self.i**2))
        return sqrt(t)

    def __add__(self, other):
        """A function to perform addition on complex numbers
        
        Args:
            other (int, complex, Complex): The second number 

        Returns:
            Complex: The result of addition
        """
        if type(other) == int:
            r = self.r + other
            result = Complex(r, self.i)
            return result
        if type(other) == complex:
            r =  int(self.r + other.real)
            i = int(self.i + other.imag)
            result = Complex(r,i)
            return result
        else:
            r = self.r + other.r
            i = self.i + other.i 
            result = Complex(r, i)
            return result
     
    def __sub__(self, other):
        """A function to perform subtraction on complex numbers
        
        Args:
            other (int, complex, Complex): The second number 

        Returns:
            Complex: The result of subtraction
        """
        if type(other) == int:
            r = self.r - other
            result = Complex(r, self.i)
            return result
        if type(other) == complex:
            r =  int(self.r - other.real)
            i = int(self.i - other.imag)
            result = Complex(r,i)
            return result
        else:
            r = self.r - other.r
            i = self.i - other.i 
            result = Complex(r, i)
            return result

    def __mul__(self, other):
        """A function to perform multiplication on complex numbers
        
        Args:
            other (int, complex, Complex): The second number 

        Returns:
            Complex: The result of multiplication
        """
        if type(other) == int:
            r = self.r * other
            i = self.i * other
            result = Complex(r,i)
            return result
        if type(other) == complex:
            r = int(self.r*other.real)-int(self.i*other.imag)
            i = int(self.r*other.imag)+int(self.i*other.real)
            result = Complex(r, i)
            return result
        else:
            r = (self.r*other.r)-(self.i*other.i)
            i = (self.r*other.i)+(self.i*other.r)
            result = Complex(r, i)
            return result

    def __eq__(self, other):
        """A function to check if two complex numbers are equal
        
        Args:
            other (Complex): The second complex number 

        Returns:
            bool: True if equal, False if not equal
        """
        if self.r == other.r and self.i == other.i:
            return True
        else:
            return False

    def __radd__(self, other):
        """A function to perform reflected addition
        
        ComplexClassObj + 3 internally means ComplexClassObj.__add__(3)  OK
        3 + ComplexClassObj means (3).__add__(ComplexClassObj) NOT OK
        Python will check if the right-hand operand implements __radd__
        If it does, it will call ComplexClassObj.__radd__(3), rather than raising a TypeError
        
        Args:
            other (int, complex, Complex): The second number 

        Returns:
            Complex: Calls __add__ and returns it's result
        """
        return Complex.__add__(self,other)
        
    def __rsub__(self, other):
        """A function to perform reflected subtraction
        
        Args:
            other (int, complex, Complex): The second number 

        Returns:
            Complex: Calls __sub__ and returns it's result
        
        """
        return Complex.__sub__(self,other)

    def __rmul__(self, other):
        """This function performs reflected multiplication

        Args:
            other (int, complex, Complex): The second number 

        Returns:
            Complex: Calls __mul__ and returns it's result
        """
        return Complex.__mul__(self,other)


