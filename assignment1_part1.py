# usr/bin/env python
# -*- coding: utf-8 -*

"""
Part 1 - Functions and Exceptions
1. Create a new python file called assignment1_part1.py. All code for this
 part should be in the file and eventually pushed to Github.
2. Create a function named listDivide that takes in two parameters. One
 parameter should have a default value of 2. The function returns the number
 of elements in the numbers list that are divisible by divide.
3. Create a custom exception class called "ListDivideException". This should
 be two lines of Python code.
4. Write another function called testListDivide that performs the following
 tests on listDivide:
   a. listDivide([1,2,3,4,5]) should returns 2
   b. listDivide([2,4,6,8,10]) should return 5
   c. listDivide([30,54,63,98,100], divide=10) should return 2
   d. listDivide([]) should return 0
   e. listDivide([1,2,3,4,5], 1) should return 5
The function testListDivide does not return anything. However, if any of the
 tests fail, -the function should raise the ListDivideException.
"""

def listDivide(numbers, divide=2):
    """Returns number of list elements divisible by divide""" 
    elementlist = []
    for number in numbers:
        if number % divide == 0:
            elementlist.append(number)
    return len(elementlist)

class ListDivideException(Exception):
    pass

def testListDivide():
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30,54,63,98,100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
    except:
        raise ListDivideException
        
if __name__ == '__main_':
    testListDivide()