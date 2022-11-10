# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 01:13:35 2022

@author: Jon


    Write a python program to find the total number of ways to make change for $1
    Examples: 100 pennies, or 75 pennies and 5 nickels
"""

coins = (50, 25, 10, 5, 1)

countWays = 0

target = int(input('(example $1 = 100) \n input an int: '))
    
for fifty in range(3): #50 cent pieces
    for quarter in range(5): #25 cent pieces
        for dimes in range(11): #10 cent pieces
            for nickels in range(51): #5 cent pieces
                for pennies in range(101): #1 cent pieces
                    amt = fifty*50 + quarter*25 + dimes*10 + nickels*5 + pennies
                    if amt == target:
                        countWays += 1
                        print(f'fifty={fifty} quarter={quarter} dimes={dimes} nickels={nickels} pennies={pennies}')

print(f'number of ways to make change for {target} is {countWays}')