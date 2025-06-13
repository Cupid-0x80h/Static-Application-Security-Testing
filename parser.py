# =================================================================
# PART 1: AST NODE CLASSES (The "Bricks")
# We define the structure of our AST nodes first.
# =================================================================

class AssignmentNode:
    """Represents assigning a value to a variable. e.g., x = 5;"""
    def __init__(self, name, value, line):
        self.name = name  # The variable being assigned to (a VariableNode)
        self.value = value # The value being assigned (e.g., a ConstantNode)
        self.line = line #and store it 

    def __repr__(self):
        # The __repr__ method gives us a nice string representation for printing.
        # Add the line number to our printout for good measure
        return f"Assignment(line:{self.line}, name={self.name}, value={self.value})"

class FunctionCallNode:
    """Represents a function call, e.g., gets("input");"""
    def __init__(self, name, args, line):
        self.name = name
        self.args = args
        self.line = line

    def __repr__(self):
        return f"FunctionCall(line:{self.line}, name={self.name.name}, args={self.args})"

class ConstantNode:
    """Represents a constant value, like a number."""
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"Constant({self.value})"

class VariableNode:
    """Represents a variable name."""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Variable({self.name})"


# =================================================================
# PART 2: THE PARSER
# Now we build the parser that uses the bricks above.
# =================================================================

import ply.yacc as yacc

# Get the list of token names from our lexer. This is required by PLY.
from lexer import tokens, lexer

# --- The Grammar Rules ---

# The starting rule. A program is a list of statements.
def p_program_statements(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]  # A list containing the first single statement
    else:
        # p[1] is the existing list of statements
        # p[2] is the new statement to add
        # We need to handle the case where a statement is None (like our return)
        if p[2] is not None:
             p[0] = p[1] + [p[2]]
        else:
             p[0] = p[1]


def p_statement_function_call(p):
    'statement : IDENTIFIER LPAREN expression RPAREN SEMICOLON'
    # For now, we are only handling calls with one argument, like gets("...")
    p[0] = FunctionCallNode(name=VariableNode(p[1]), args=[p[3]], line=p.lineno(1))

# We also need to teach 'expression' to be a STRING
def p_expression_string(p):
    'expression : STRING'
    p[0] = ConstantNode(p[1])


# Grammar rule for an assignment statement. e.g., score = 100;
def p_statement_assign(p):
    '''statement : IDENTIFIER ASSIGN expression SEMICOLON
                 | INT_KEYWORD IDENTIFIER ASSIGN expression SEMICOLON'''
    # This logic handles both cases
    if len(p) == 5:
        # p.lineno(1) gets the line number of the FIRST token (the identifier)
        p[0] = AssignmentNode(name=VariableNode(p[1]), value=p[3], line=p.lineno(1))
    else:
        # p.lineno(2) gets the line number of the SECOND token (the identifier)
        p[0] = AssignmentNode(name=VariableNode(p[2]), value=p[4], line=p.lineno(2))


# Grammar rule for a return statement.
def p_statement_return(p):
    'statement : RETURN expression SEMICOLON'
    # For now, we'll just print that we saw a return statement.
    # In a real compiler, we'd create a ReturnNode.
    print(f"Parser saw a return statement with value: {p[2]}")
    p[0] = None # This statement doesn't add a node to our AST for now.

# Grammar rule for what an 'expression' can be. For now, it's just a number.
def p_expression_number(p):
    'expression : NUMBER'
    # Create a ConstantNode for the number.
    p[0] = ConstantNode(p[1])

# Rule to handle syntax errors.
def p_error(p):
    if p:
        print(f"Syntax error at token: {p.type} ('{p.value}') on line {p.lineno}")
    else:
        print("Syntax error at end of input")

# --- Build the Parser ---
# This command tells PLY to read all our rules and create the parser.
parser = yacc.yacc()


# =================================================================
# PART 3: TESTING THE PARSER
# =================================================================

if __name__ == '__main__':
    from analyzer import SecurityAnalyzer
    # Our sample code with a few variables.
    sample_code = """
int secret_key = 12345;
gets("user_input");
return 0;
"""
    # NOTE: Our parser currently ignores the 'int' keyword, but that's okay for our goal.
    # We are only looking for assignments right now.
    
    # Use the parser on our sample code.
    try:
        # The parser.parse() function takes the full code string as input.
        # It will automatically use the lexer behind the scenes.
        ast = parser.parse(input=sample_code, lexer=lexer)
        
        print("\n--- Abstract Syntax Tree ---")
        if ast:
            for statement in ast:
                print(statement)
            
        # --- RUN THE SECURITY ANALYSIS ---
        print("\n--- Security Analysis ---")
        analyzer = SecurityAnalyzer()
        warnings = analyzer.analyze(ast)

        if warnings:
            print("Found security warnings:")
            for warning in warnings:
                print(f"  - {warning}")
        else:
            print("No security warnings found. Code looks good!")
            
    except Exception as e:
        print(f"An error occurred: {e}")