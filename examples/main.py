#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:39:04 2020

@author: akel
"""

import numpy as np
import argparse
import load1 as l1


parser = argparse.ArgumentParser()
parser.add_argument("inp", help="input file",type=str)
args = parser.parse_args()
A=l1.input_1(args.inp)
print(l1.input_1(args.inp))

