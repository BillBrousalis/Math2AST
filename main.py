#!/usr/bin/env python3
from lexer import *
from parser import *
from util import *
from ast_eval import node_eval
import glob
import sys
import os

PLOT = os.getenv('PLOT', '') == '1'

def run(fname):
  print(f'[*] Testing {fname}')
  with open(fname, 'r') as f:
    text = f.read().strip()
  lex = Lexer()
  lex.tokenize(text)
  lex.print_tokens()

  parser = Parser(lex)
  root = parser.parse()
  result = node_eval(root)
  print(f'Result = {result}')
  if PLOT: plot(root, fname)

if __name__ == '__main__':
  if len(sys.argv) >= 2:
    run(sys.argv[1])
  else:
    for fname in glob.glob('tests/*.txt'):
      run(fname)
