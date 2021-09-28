"""
I'm working on writing math formulas in python, but I'm having trouble. Can you help me fix them?

Operations in Python:
    addition: a+b
    subtraction: a-b
    negation: -a
    multiplication: a*b
    division: a/b
    integer division: a//b (returns a/b with the decimals chopped off)
    exponentiation: a**b (returns a to the b power)

"""
import numpy as np

def skware(x):
    """sometimes I want to get something times itself
    """
    a= x**2
    return a

def cube(x):
    """
    sometimes I want something times itself, times itself
    """
    return x**3
    

def quadratic_solver(coefficients):
    """
    coefficients is a list of length 3, [a,b,c],
    where a,b,c correspond to ax^2+bx+c=0
    should return the two solutions to the quadratic formula
    """
    complex_nums=[complex(i) for i in coefficients] #Make sure we can get all soln, not just reals
    a=complex_nums[0]
    b=complex_nums[1]
    c=complex_nums[2]

    lead = -b/a
    discriminant = np.sqrt(b**2-4*a*c)
    tail = discriminant/a

    x1 = lead+tail
    x2 = lead-tail
    return x1 #How do I return both x1 and x2

def calc_circumference(r):
    """I need the circumference of a circle, given its radius, r
    """
    return np.pi*r**2

def calc_area(r):
    """I need the area of a circle, given its radius, r
    """
    return np.pi*r*2
#branchcheck
print(cube(2))
