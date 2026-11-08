import os
from tree_sitter import Language, Parser
import tree_sitter_c as tsc

def parse_c_source(file_path: str):
    # Initialize Tree-sitter for C language
    C_LANGUAGE = Language(tsc.language())
    parser = Parser(C_LANGUAGE)
    
    if not os.path.exists(file_path):
        print(f"[Error] File not found: {file_path}")
        return None

    with open(file_path, "rb") as f:
        tree = parser.parse(f.read())
        
    print(f"[Parser] Successfully parsed AST for {file_path}")
    return tree

if __name__ == "__main__":
    # Test on a dummy file or main.py
    print("Parser module ready.")