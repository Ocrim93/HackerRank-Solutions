#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'Escape' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY galaxy
#  2. INTEGER fuel
#
class Star:
    def __init__(self,amount_fuel, stars = []):
        self.amount_fuel = amount_fuel
        self.stars = stars
        
    
    def move(self):
        if self.stars[0] < self.stars[1]:
            return (self.amount_fuel,0)
        else :
            return (self.amount_fuel,1) 

def check_right_side(galaxy,fuel):
    spent_fuel = 0
    for el in galaxy:
        spent_fuel += el[-1].amount_fuel

    if fuel > spent_fuel:
        return True

def escape(galaxy, fuel):
    # g [[Star]]
    g = make_galaxy(galaxy)

    
    path_fuel = 0
    spent_fuel = 0
    index = 0
    layer = 0

    
    breadcrumbs = [] # store the indexes per layer
   
    path_found = False
    previous_layer = False
    go_back = 0
    go_back_temp = 0
    check_previous = False

    while not path_found:
        breadcrumbs.append(index)
        print(layer,index)
        star = g[layer][index]
        spent_fuel += star.amount_fuel
        if star.stars != []:
            path_fuel,star_choice = star.move() # cost to move to the minimum connected star (amount_fuel, star_idx)
           
        if spent_fuel + path_fuel < fuel and star.stars == []:
            path_found = True
            index = index + star_choice
            spent_fuel  +=  path_fuel
            breadcrumbs.append(index)
            return "ESCAPED"    
        if spent_fuel + path_fuel < fuel and star.stars != []:
            layer += 1
            index = index + star_choice
            #breadcrumbs.append(index)
            continue
       
        if spent_fuel + path_fuel > fuel and (layer,index) not in [(len(g)-1,len(g[-1])-2),(0,0)]:

            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",breadcrumbs,go_back)
            
            if check_previous:
                go_back = go_back_temp 
                check_previous = False
            else:
                check_previous = True
                go_back = 0  
                
            h = len(breadcrumbs)
            if star.stars != []:
                go_back = 0
            for i in range(1,3+go_back,1):
                spent_fuel -= g[h-i][breadcrumbs[-i]].amount_fuel
            
            
            if breadcrumbs[-(2+go_back)] -  breadcrumbs[-(3+go_back)] == 0:
                index = breadcrumbs[-(2+go_back)] +1 
            else:
                index = breadcrumbs[-(2+go_back)] -1 
            for i in range(2+go_back):
                breadcrumbs.pop(-1)
            go_back += 1
            go_back_temp += 1
            layer -= go_back
            if layer == 1:
                go_back =0
                go_back_temp= 0
                     
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",breadcrumbs)    
        elif (layer,index) == (0,0) or check_right_side(g,fuel):
            return "TRAPPED"   
        else:
            return "TRAPPED"    
             

            

    

# fuel_array => 2D list of integers representing the fuel for each star in the galaxy      
def make_galaxy(fuel_array) -> [[Star]]:
    """Produce a galaxy from an fuel_array of star fuel amounts,
    
    e.g to produce the example from the question definition
        g = makeGalaxy([[15],[2,3],[40,5,6],[1,5,15,12]])
    """
    h = len(fuel_array)
    if(h == 0):
        return None
    galaxy = [[Star(g) for g in fuel_array[i]] if i == h-1 else [None] for i in range(h)]
   
    for l in range(h-2,-1,-1):
        galaxy[l] = [Star(g,[galaxy[l+1][i].amount_fuel,galaxy[l+1][i+1].amount_fuel]) for i,g in enumerate(fuel_array[l])]
    
    return galaxy

        
   
s = [[15],[2,3],[1,2,3],[1,2,3,4],[i for i in range(1,6,1)],[50,1,48,47,46,50]]





print(escape(s,50  ))
    
