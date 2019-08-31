#!/usr/bin/python
#< ----------- Starts the ManipuLogic program up ----------- >

""" Program-level TODOs:
    1.) Check all comments for clarity
    2.) Create CLI interation
    3.) Create GUI interaction
    4.) Refactor such that classes, functions, data, and control flow
        are abstracted away to account for 1st order logic.
"""

import sys
sys.path.append('Classes')
from Propositions import *

#from tkinter import Tk
#from tkinter.filedialog import askopenfilename
#Tk().withdraw()
#filename = askopenfilename()
#with open(filename) as file:
#    with file.readlines() as lines:
#        for line in lines:
#            try:
#                print(line)
#                exec(line)
#            except Exception as e:
#                pass
def pr():
    print("CP " + ~cp)
    print("")

p = SimpleProp("P")
q = SimpleProp("Q")
cp = -(p + q)
pr()
cp = -cp
pr()
cp = p > q
pr()
cp = -cp
pr()
cp = --p&q>-p
pr()
cp = -(-p&q>-p)
pr() #TODO goof around with this some more!


#p = SimpleProp("Socrates is a man.")
#q = SimpleProp("2 + 2 = 5")
#cp = -p
#pr()
#cp = -cp
#pr()

#cp = -(p > q)
#pr()

#cp = -(p + q)
#pr()
#print(p == p)
#print (p == cp)


