# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:47:53 2025

@author: jackm
"""
from Line import Line

def find_grid(lines):
    if lines[0] is not None:
        for line in lines:
            if line.length() > 10 and line.length() < 100:
                return line
        