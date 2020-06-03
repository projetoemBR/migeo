#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:39:04 2020

@author: akel
exemplo simples da função argparse para leitura de arquivo em linha
de comando.
$python3 main.py dado.dat
"""
import argparse
import load1 as l1


parser = argparse.ArgumentParser()
parser.add_argument("inp", help="input file",type=str)
args = parser.parse_args()
print(l1.input_1(args.inp))

