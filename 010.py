'''
You are asked to ensure that the first and last names of people begin with a capital letter 
in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.
'''
import math
import os
import random
import re
import sys


def solve(s):
    '''
    function to capitalize first letter of each word if it is a letter.
    '''
    return ' '.join([i[0].upper() + i[1:] for i in s.split()])


if __name__ == '__main__':
    # s = "1 w 2 r 3g"
    # s = "allision heck"
    s = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"

    result = solve(s)

    print(result)
