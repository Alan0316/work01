# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:58:57 2024

@author: Student
"""

# Truth values for P and Q
P_values = [False, False, True, True]
Q_values = [False, True, False, True]

# Logical operations
def conjunction(P, Q):
    return P and Q

def disjunction(P, Q):
    return P or Q

def implication(P, Q):
    return not P or Q

def biconditional(P, Q):
    return (not P or Q) and (not Q or P)

# Displaying the truth table
print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format("P", "Q", "P∧Q", "P∨Q", "P→Q", "P←Q", "P↔Q"))
for P, Q in zip(P_values, Q_values):
    print("{:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}".format(str(P), str(Q), str(conjunction(P, Q)), str(disjunction(P, Q)), str(implication(P, Q)), str(implication(Q, P)), str(biconditional(P, Q))))
