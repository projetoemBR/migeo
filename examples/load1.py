#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:56:12 2020

@author: akel
"""

import numpy as np

def input_1(filename):
    """ Leitura arquivo input"""
#    filename=input()
    return np.loadtxt(filename)


if __name__ == "__main__":
    import sys
    print(input_1(str(sys.argv[1])))
    