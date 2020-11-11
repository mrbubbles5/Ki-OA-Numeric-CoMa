from os import system

import numpy as np
import random

system('cls')

c = int(input("Geben sie einen Zahlwert ein\n"))
system('cls')

n = int(input("Geben sie die Dimension des Vektors als Integer ein\n"))
system('cls')

def new_input():
    #c = int(input("Geben sie einen Zahlwert ein\n"))
    #if type(c)!= float or type(c)!= int:
    
    #n = int(input("Geben sie die Dimension des Vektors als Integer ein\n"))

    x_el = random.uniform(-1, 1)
    x = np.array([x_el for i in range(n)])
    c_diag = np.array([c**((i-1)/(n-1)) for i in range(n)])

    C = np.diag(c_diag)
    
    return C, x

def sq():
    C,x = new_input()
    
    for i in range(n):
        for j in range(n):
            C[j][i] = C[j][i] * x[j]
    
    for i in range(n):
         for j in range(n):
             C[i][j] = C[i][j] * x[j]

    return C

def hole():
    a = input("Geben sie eine Konstante a ein\n")
    system('cls')
    
    dummy = sq()
    inv_dummy = np.linalg.inv(dummy)
    
    return np.matmul(dummy, inv_dummy)
    
    
