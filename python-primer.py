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


"""
C-1.16
In our implementation of the scale function (page 25 
def scale(data, factor):
for j in range(len(data)):
data[j] = factor))
the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
"""

#solution

# In Python, when we pass a mutable object (like a list) to a function, we are passing a reference to that object, not a copy of it.
def scale(data, factor):
    for j in range(len(data)):
        data[j] = factor  # This modifies the elements of the list in place, which affects the original list passed by the caller.

data = [1, 2, 3]
scale(data, 2)
print(data)  # Output will be [2, 2, 2], showing that the original list was modified.


"""
C-1.17
Had we implemented the scale function (page 25) as follows, does it work
properly?
def scale(data, factor):
    for val in data:
         val *= factor
Explain why or why not.
"""

#solution
"""
This implementation does not work properly because `val` is a local variable
that holds a copy of each element in the list `data`.
Modifying `val` does not change the original elements in `data`. 
Therefore, the original list remains unchanged after the function call."""


"""
C-1.18
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
"""

#solution
# it uses list comprehension to produce the desired list of numbers based on the formula n*(n-1) for n in range(10)
print([n*(n+1) for n in range(10)])

#or
"""
l=[]
for n in range(10):
    v=n*(n+1)
    l.append(v)
print(l)
"""



"""
C-1.19
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
"""

#solution
# it uses list comprehension to produce the desired list of lowercase letters from 'a' to 'z'
# using the chr function and ASCII values

print([chr(i) for i in range(ord('a'), ord('z') + 1)])

#or
"""
l=[]
for i in range(ord('a'), ord('z') + 1):#for i in range(97, 123):
    l.append(chr(i))
print(l)
"""


"""
C-1.20
Python’s random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possi-
ble order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

#solution


def my_shuffle(data):
    # it shuffles the list by iterating through the list in reverse order and swapping each element with
    # a randomly chosen element from the portion of the list that has not yet been shuffled
    for i in range(len(data) - 1, 0, -1):
        j = random.randint(0, i)
        data[i], data[j] = data[j], data[i]

data = [1, 2, 3, 4, 5]
my_shuffle(data)
print(data)



"""
C-1.21
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

#solution
def read_lines_reverse():
    # it reads lines from standard input until an EOFError is raised, and then outputs those lines in reverse order
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    for line in reversed(lines):
        print(line)
        


"""
C-1.22 
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i]= a[i] · b[i], for i = 0,...,n−1.
"""

#solution
def dot_product(a, b):
    # it calculates the dot product of two arrays a and b by multiplying corresponding elements and storing the results in a new array c
    if len(a) != len(b):
        raise ValueError("Arrays must be of the same length")
    
    c = [a[i] * b[i] for i in range(len(a))]
    return c

a = [int(x) for x in input("Enter elements of array a separated by space: ").split()]
b = [int(x) for x in input("Enter elements of array b separated by space: ").split()]
print(dot_product(a, b))    


"""
C-1.23
Give an example of a Python code fragment that attempts to write an element
 to a list based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message:
“Don’t try buffer overflow attacks in Python!”"""

#solution
try:
    lst = [1, 2, 3]
    index = int(input("Enter an index to write to the list: "))
    lst[index] = 10  # Attempting to write to the list at the given index

except IndexError:
    print("Don’t try buffer overflow attacks in Python!")


"""
C-1.24
Write a short Python function that counts the number of vowels in a given
character string.
"""

#solution
def count_vowels(s):
    # it counts the number of vowels in the given string s by iterating through each character and checking if it is a vowel
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

s = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(s)}")


""
"""
C-1.25
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let s try, Mike.", this function would return
"Lets try Mike".
"""

#solution

def remove_punctuation(s):
    # it removes all punctuation from the given string s by iterating through each character and keeping only alphanumeric characters and spaces
    return ''.join(char for char in s if char.isalnum() or char.isspace())

s = input("Enter a string: ")
print(f"String with punctuation removed: {remove_punctuation(s)}")


"""
C-1.26
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a+b = c,” “a = b−c,” or “a ∗ b = c.”
"""

#solution
def check_arithmetic_formula(a, b, c):
    # it checks if the three integers a, b, and c can be used in a correct arithmetic formula in the given order
    if a + b == c:
        return f"{a} + {b} = {c}"
    elif a == b - c:
        return f"{a} = {b} - {c}"
    elif a * b == c:
        return f"{a} * {b} = {c}"
    else:
        return "No valid arithmetic formula found."

a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))
print(check_arithmetic_formula(a, b, c))


"""
C-1.27
In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementa-
tions, from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance ad-
vantages."""

#solution
def factors(n):
    # it generates the factors of the given integer n in increasing order
    small_factors = []
    large_factors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            small_factors.append(i)
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                large_factors.append(n // i)
    
    # Yield small factors first, then large factors in reverse order
    for factor in small_factors:
        yield factor
    for factor in reversed(large_factors):
        yield factor


"""
C-1.28
C-1.28 The p-norm of a vector v =(v1,v2,...,vn) in n-dimensional space is de-
fined as
||v|| = ᵖ√(v₁ᵖ + v₂ᵖ + ... + vₙᵖ).
For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Eu-
clidean norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of √42 +32 = √16+9 = √25 = 5.
 Give an implementation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
"""

#solution
def norm(v, p):
    # it calculates the p-norm of the vector v by summing the p-th powers of its elements and taking the p-th root
    return sum(abs(x) ** p for x in v) ** (1 / p)

v = [4, 3]
p = 2
print(f"The {p}-norm of the vector {v} is: {norm(v, p)}")





"""----------------------------------------PROJECTS--------------------------------------------"""




"""
P-1.29
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
"""

#solution

def generate_strings():
    characters = ['c', 'a', 't', 'd', 'o', 'g']
    all_permutations = permutations(characters)
    for perm in all_permutations:
        print(''.join(perm))

generate_strings()


"""
P-1.30
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
"""

#solution
def divide_until_less_than_two(n):
    # it counts the number of times n can be divided by 2 before it becomes less than 2
    count = 0
    while n >= 2:
        n /= 2
        count += 1
    return count

n = int(input("Enter a positive integer greater than 2: "))
if n > 2:
    print(f"Number of times to divide {n} by 2 before getting a value less than 2: {divide_until_less_than_two(n)}")
else:
    print("Please enter a positive integer greater than 2.")    


"""
P-1.31
Write a Python program that can “make change.” Your program should
take two numbers as input, one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible."""

#solution
def make_change(charged, given):
    # it calculates the change to be given back and returns the number of each kind of bill and coin needed to make that change
    change = given - charged
    if change < 0:
        return "Insufficient amount given."
    
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]  # Example denominations in dollars
    change_dict = {}
    
    for denom in denominations:
        count = int(change // denom)
        if count > 0:
            change_dict[denom] = count
            change -= count * denom
    
    return change_dict

charged = float(input("Enter the amount charged: "))
given = float(input("Enter the amount given: "))
change = make_change(charged, given)
if isinstance(change, str):
    print(change)
else:
    print("Change to be given back:")
    for denom, count in change.items():
        print(f"${denom:.2f}: {count} piece(s)")



"""
P-1.32
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""

#solution
def simulate_calculator():
    # it simulates a simple calculator that takes numbers and operators as input and displays the result after each input
    current_value = 0
    operator = None
    
    while True:
        user_input = input("Enter a number or operator (+, -, *, /, =): ")
        
        if user_input in ['+', '-', '*', '/']:
            operator = user_input
        elif user_input == '=':
            print(f"Result: {current_value}")
            current_value = 0
            operator = None
        else:
            try:
                number = float(user_input)
                if operator is None:
                    current_value = number
                else:
                    if operator == '+':
                        current_value += number
                    elif operator == '-':
                        current_value -= number
                    elif operator == '*':
                        current_value *= number
                    elif operator == '/':
                        if number != 0:
                            current_value /= number
                        else:
                            print("Error: Division by zero.")
                            continue
                print(f"Current value: {current_value}")
            except ValueError:
                print("Invalid input. Please enter a number or an operator.")


simulate_calculator()


"""
P-1.33
Write a Python program that simulates a handheld calculator. Your pro-
gram should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each op-
eration is performed. Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
"""

#solution
def handheld_calculator():
    # it simulates a handheld calculator that processes button inputs and displays the result after each operation
    current_value = 0
    operator = None
    
    while True:
        user_input = input("Enter a number, operator (+, -, *, /), or 'C' to clear: ")
        
        if user_input in ['+', '-', '*', '/']:
            operator = user_input
        elif user_input.upper() == 'C':
            current_value = 0
            operator = None
            print("Calculator cleared. Current value: 0")
        else:
            try:
                number = float(user_input)
                if operator is None:
                    current_value = number
                else:
                    if operator == '+':
                        current_value += number
                    elif operator == '-':
                        current_value -= number
                    elif operator == '*':
                        current_value *= number
                    elif operator == '/':
                        if number != 0:
                            current_value /= number
                        else:
                            print("Error: Division by zero.")
                            continue
                print(f"Current value: {current_value}")
            except ValueError:
                print("Invalid input. Please enter a number, an operator, or 'C' to clear.")
    
handheld_calculator()


"""
P-1.34
A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos."""

#solution
def spam_friends():
    # it writes out the sentence "I will never spam my friends again." one hundred times, numbering each sentence and introducing random typos
    import random
    
    sentence = "I will never spam my friends again."
    typos = ["I will never spam my frinds again.", "I will never spam my frends again.", 
             "I will never spam my frieneds again.", "I will never spam my frineds again.", 
             "I will never spam my frinds agian.", "I will never spam my frends agian.", 
             "I will never spam my frieneds agian.", "I will never spam my frineds agian."]
    
    for i in range(1, 101):
        if i % 12 == 0:  # Introduce a typo every 12 sentences
            typo = random.choice(typos)
            print(f"{i}: {typo}")
        else:
            print(f"{i}: {sentence}")
            
spam_friends()


"""
p-1.35
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100.
"""

#solution

import random

def generate_birthdays(n):
    return [random.randint(1, 365) for _ in range(n)]

def has_duplicate(birthdays):
    return len(birthdays) != len(set(birthdays))

def test_birthday_paradox():
    for n in range(5, 101, 5):
        count = 0
        for _ in range(1000):  # Run 1000 experiments
            birthdays = generate_birthdays(n)
            if has_duplicate(birthdays):
                count += 1
        probability = count / 1000
        print(f"n = {n}, Probability = {probability:.2f}")
n=int(input("Enter the number of people in the room (n): "))
test_birthday_paradox()



