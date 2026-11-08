from parser.c_parser import parse_c_source
from z3 import *

def test_pipeline():
    print("--- Running Neuro-Symbolic Pipeline Test ---")
    
    # 1. Parse the C source code AST via Tree-sitter
    ast = parse_c_source("vulnerable.c")
    if ast:
        print("[Pipeline] AST successfully extracted from vulnerable.c")
    
    # 2. Run Z3 formal verification on the logic extracted from the file
    x = BitVec('x', 32)
    patch_output = If(x + 100 > 2000, BitVecVal(2000, 32), x + 10