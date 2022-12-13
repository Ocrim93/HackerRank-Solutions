#!/bin/python3

import math
import os
import random
import re
import sys
import random 


#
# Complete the 'entryTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING keypad
#

import numpy as np

def build_matrix(keypad):
    arr = np.array(list(keypad),dtype='i')
    matrix = arr.reshape(3,3)
    return matrix 
        
def func(x):
    arr = []
    if x ==0:
        arr = [0,1]
    if x == 1:
        arr = [0,1,2]
    if x == 2:
        arr = [1,2]        
    return arr

def find_the_adjacent(matrix,number):
    arr_adj = []    
    coord_numb = (int(np.where(matrix == number)[0]), int(np.where(matrix == number)[1]))
    if coord_numb == (1,1):
        for i in range(1,10):
            if i == number:
                continue 
            arr_adj.append(i)
        return arr_adj
    
    arr1 = func(coord_numb[0])
    arr2 = func(coord_numb[1])

    set_combinations = set()

    for i in arr1:
        for j in arr2:
            set_combinations.add((i,j))
    set_combinations.remove(coord_numb)

    for el in set_combinations:
        arr_adj.append(matrix[el[0]][el[1]])
    return arr_adj    
    




    
def entryTime(s, keypad):
    matrix = build_matrix(keypad)
    sequence =[]
    
    for el in s:
        sequence.append(int(el))
    counter = 0
    sequence_no_duplicate_adj = []

    for i,el in enumerate(sequence):
        if i ==0 :
            sequence_no_duplicate_adj.append(el)
            continue
        if el == sequence[i-1]:
            continue 
        else:
            sequence_no_duplicate_adj.append(el)

    sequence = sequence_no_duplicate_adj      

  
    for i,number in enumerate(sequence):
        
        if i ==0:
            continue

        adj = number
        if adj in  find_the_adjacent(matrix,sequence[i-1]) :
            counter += 1
            continue 
        else:
            counter +=2
    return  counter    



def random_choice(length):

    list_number = list(range(1,10))
    keypad = ''
    s = ''
    while  len(list_number) >0:
        selection = random.choice(list_number)
        keypad += str(selection)
        list_number.remove(selection)
    counter = 0 
    while counter < length:
        s += str(random.choice(range(1,10)))
        counter += 1

    return keypad,s

    

if __name__ == '__main__':
    

    length = 4
    keypad,s = random_choice(length)
    matrix = build_matrix(keypad)
    
    print(matrix)
    print(s)

    

    result = entryTime(s, keypad)

    print(result)
