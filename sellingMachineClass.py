#!/bin/python3

import math
import os
import random
import re
import sys


class VendingMachine:
    # Imdef __init__(self, name, age):plement the VendingMachine here
    def __init__(self, num_items, item_price):
        self.num_items = num_items
        self.item_price = item_price
    def buy(self,req_items,money):
        print()
        print(self.num_items,self.item_price,req_items,money)
        print((self.item_price)*req_items >= money )
        if self.num_items >= req_items and (self.item_price)*req_items <= money :
            self.num_items = self.num_items - req_items
            return self.num_items
        if not (self.item_price)*req_items >= money:
            raise ValueError('Not enough coins')
        if self.num_items < req_items:
            raise ValueError('Not enough items in the machine')
        
            
if __name__ == '__main__':


    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
           
        except ValueError as e:
            print(e)


