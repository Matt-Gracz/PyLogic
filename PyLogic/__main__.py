#!/usr/bin/python
#< ----------- Starts the PyLogic program up ----------- >

""" Program-level TODOs:
    1.) Check all comments for clarity
    2.) Create CLI interation
    3.) Create GUI interaction
    4.) Refactor such that classes, functions, data, and control flow
        are abstracted away to account for 1st order logic.
"""

import sys
sys.path.append('Classes')
from BaseClasses import *
from Propositions import *
from Operators import *

p = SimpleProp("P")
q = SimpleProp("Q")
cp = p & q | p > p | q


print(cp)

