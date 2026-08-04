#exercise solutions for python primer
#Reinforcement
"""
R-1.1 
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise."""

#solution
def is_multiple(n,m):
    # it checks if n is a multiple of m by checking if the remainder of n divided by m is zero
    if n%m==0:
        return True
    else:
        return False

n=int(input("Enter the first number: "))
m=int(input("Enter the second number: "))
print(is_multiple(n,m))

"""
R-1.2
Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""

#solution
def is_even(k):
    # it checks if k is even by checking if the last digit of k is 0, 2, 4, 6, or 8
    if str(k)[-1] in ['0', '2', '4', '6', '8']:
        return True
    else:
        return False

K=int(input("Enter a number: "))
print(is_even(K))

"""
R-1.3
Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

#solution

def minmax(data):
    # it initializes the minimum and maximum values to the first element of the data
    min_val = data[0]
    max_val = data[0]
    
    # it iterates through the data to find the minimum and maximum values
    for num in data:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
            
    return (min_val, max_val)

data = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(minmax(data))

"""
R-1.4
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""

#solution
def sum_of_squares(n):
    # to calculates the sum of all squares of positive intergers samaller than n
    total=0
    for i in range (1,n):
        total +=i**2
        return total 

n=int(input("Enter a positive integer: "))
print(sum_of_squares(n))

"""
R-1.5
Give a single command that computes the sum from Exercise R-1.4, 
relying on Python’s comprehension syntax and the built-in sum function.
"""

#solution
n = int(input("Enter a positive integer: "))
print(sum(i**2 for i in range(1, n)))   