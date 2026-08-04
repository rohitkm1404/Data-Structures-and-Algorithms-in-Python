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


"""
R-1.6 
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.
"""

#solution
def sum_of_odd_squares(n):
    # it calculates the sum of squares of all odd positive integers smaller than n
    total = 0
    for i in range(1, n):
        if i % 2 != 0:
            total += i ** 2
    return total

n = int(input("Enter a positive integer: "))
print(sum_of_odd_squares(n))

"""
R-1.7
Give a single command that computes the sum from Exercise R-1.6,
relying on Python’s comprehension syntax and the built-in sum function.
"""

#solution
n = int(input("Enter a positive integer: "))
# it computes the sum of squares of all odd positive integers smaller than n using comprehension syntax and the built-in sum function
print(sum(i**2 for i in range(1, n) if i % 2 != 0))

"""
R-1.8
Python allows negative integers to be used as indices into a sequence,
such as a string. If string s has length n, and expression s[k] is used for index
-n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
the same element?"""

#solution
def negative_index_to_positive(s, k):
    # it converts a negative index k to its equivalent positive index j
    n = len(s)
    if -n <= k < 0:
        j = n + k
        return j
    else:
        raise IndexError("Index out of range")

s = input("Enter a string: ")

k = int(input("Enter a negative index: "))
try:
    j = negative_index_to_positive(s, k)
    print(f"The equivalent positive index is: {j}")        

except IndexError as e:
    print(e)    

"""
R-1.9
What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80?"""

#solution
# it uses the range constructor with start=50, stop=90, step=10 to produce the desired range
print(list(range(50, 90, 10)))
#or 
"""
for i in range(50, 90, 10):
    print(i,end=" ")
    """


"""
R-1.10
What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""

#solution
# it uses the range constructor with start=8, stop=-10, step=-2 to produce the desired range
print(list(range(8, -10, -2)))
#or
"""for i in range(8, -10, -2):
    print(i,end=" ")"""


"""
R-1.11
Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""

#solution
# it uses list comprehension to produce the desired list of powers of 2
print([2**i for i in range (0,9)])
#or 
"""for i in range(0, 9):
    print(2**i,end=" ")"""

"""
R-1.12
Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module includes 
a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function."""

#solution

import random
def my_choice(data):
    return data[random.randrange(len(data))]





#-----------------------------------------creativity problems---------------------------------------------





"""
C-1.13
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

#solution
def reverse_list(data):
    # it reverses the list by swapping elements from the start and end of the list
    n = len(data)
    for i in range(n // 2):
        data[i], data[n - 1 - i] = data[n - 1 - i], data[i]
    return data


"""
C-1.14
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

#solution
def has_odd_product_pair(data):
    # it checks if there is a distinct pair of numbers in the sequence whose product is odd
    odd_numbers = [num for num in data if num % 2 != 0]
    return len(odd_numbers) >= 2


data = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(has_odd_product_pair(data))

#or 
"""def has_odd_product_pair(data):
    # it checks if there is a distinct pair of numbers in the sequence whose product is odd
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] % 2 != 0 and data[j] % 2 != 0:
                return True
    return False"""

data = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(has_odd_product_pair(data))

"""
C-1.15
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
"""

#solution
def are_all_distinct(data):
    # it checks if all the numbers in the sequence are distinct by comparing the length of the set of data with the length of the original data
    return len(data) == len(set(data))


data = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(are_all_distinct(data))




