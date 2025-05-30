from lexer import lexer 
from parser import parser
from semantic import SemanticAnalyzer
from ir_generator import IRGenerator
from optimizer import Optimizer
from executor import Executor
import io
import sys

def run_code_with_compiler(user_code: str):
    
    old_stdout = sys.stdout
    sys.stdout = mystdout = io.StringIO()

    try:
        
        lexer.input(user_code)

       
        ast = parser.parse(user_code, lexer=lexer)

        
        SemanticAnalyzer().analyze(ast)

       
        ir = IRGenerator()
        ir.generate(ast)

       
        opt = Optimizer(ir.code)
        opt.optimize()

       
        result = Executor(opt.get_code)
        result.run()
    except Exception as e:
        print("error", e)

    sys.stdout = old_stdout

    
    return mystdout.getvalue()
