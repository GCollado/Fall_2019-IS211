# user/bin/env python
# -*- coding: utf-8 -*-

"""
Part II - Simple Class
1. Create a new python file called assignment1_part2.py. All code for
 this part should be in this file and eventually pushed to Github
2. Create a class called Book. The class should have the following 
properties:
a. Two attributes, author and title, both should be initialized to the
 blank string
b. An __init__ function that takes in an author and a title, and sets
 them to the object variables
c. A function called displays, which when called, simply print out a
 string representing the book. The output should be in the form of 
 "title, written by author."
 Example: "Of Mice and Men, written by John Steinbeck."
3. Instantiate two objects from this class. The first object represents
 the book 'Of Mice and Men', written by John Steinbeck; the other is
 'To Kill a Mockingbird' by Harper Lee.'
4. Print both of these objects to the screen by calling their display() 
functions.
"""

class Book():
    def __init__(self,author, title):
        self.author = author
        self.title = title

    def display(self):
        print(self.title + ", written by " + self.author)
    
js = Book('John Steinbeck', 'Of Mice and Men')
hl = Book('Harper Lee', 'To Kill a Mockingbird')

if __name__ == "__main__":
    js.display()
    hl.display()