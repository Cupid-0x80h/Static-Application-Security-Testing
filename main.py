from lexer import lexer
from parser import parser
from analyzer import SecurityAnalyzer

# The sample code to be analyzed
sample_code = """
int admin_password = 456;
char buffer[10];
strcpy(buffer, "user_data");
"""

def main():
    print("--- Starting SAST Tool ---")
    try:
        ast = parser.parse(sample_code, lexer=lexer)
        
        if not ast:
            print("Could not generate AST. Please check for syntax errors.")
            return

        print("\n--- Abstract Syntax Tree ---")
        for statement in ast:
            print(statement)
        
        print("\n--- Security Analysis ---")
        analyzer = SecurityAnalyzer()
        warnings = analyzer.analyze(ast)

        if warnings:
            print("Found security warnings:")
            for warning in warnings:
                print(f"  - {warning}")
        else:
            print("No security warnings found.")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
