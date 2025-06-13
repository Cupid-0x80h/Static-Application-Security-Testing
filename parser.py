import ply.yacc as yacc
from lexer import tokens, lexer

# --- AST Node Classes ---
class AssignmentNode:
    def __init__(self, name, value, line):
        self.name = name; self.value = value; self.line = line
    def __repr__(self):
        return f"Assignment(line:{self.line}, name={self.name}, value={self.value})"

class DeclarationNode:
    def __init__(self, var_type, name, size=None, line=0):
        self.var_type = var_type; self.name = name; self.size = size; self.line = line
    def __repr__(self):
        if self.size: return f"Declaration(line:{self.line}, type:{self.var_type}, name:{self.name}, size:{self.size})"
        return f"Declaration(line:{self.line}, type:{self.var_type}, name={self.name})"

class FunctionCallNode:
    def __init__(self, name, args, line):
        self.name = name; self.args = args; self.line = line
    def __repr__(self):
        return f"FunctionCall(line:{self.line}, name={self.name.name}, args={self.args})"

class ConstantNode:
    def __init__(self, value): self.value = value
    def __repr__(self): return f"Constant({self.value})"

class VariableNode:
    def __init__(self, name): self.name = name
    def __repr__(self): return f"Variable({self.name})"

# --- Grammar Rules ---
def p_program_statements(p):
    'program : statement_list'
    p[0] = p[1]

def p_statement_list(p):
    'statement_list : statement_list statement'
    if p[2]: p[0] = p[1] + (p[2] if isinstance(p[2], list) else [p[2]])
    else: p[0] = p[1]

def p_statement_list_single(p):
    'statement_list : statement'
    p[0] = p[1] if isinstance(p[1], list) else [p[1]]

def p_statement(p):
    '''statement : assignment_statement
                 | declaration_statement
                 | function_call_statement
                 | return_statement'''
    p[0] = p[1]

def p_declaration_statement(p):
    '''declaration_statement : type_specifier IDENTIFIER SEMICOLON
                             | type_specifier IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON
                             | type_specifier IDENTIFIER ASSIGN expression SEMICOLON'''
    var_type = p[1]
    name_node = VariableNode(p[2])
    line = p.lineno(2)
    if len(p) == 4:
        p[0] = DeclarationNode(var_type, name_node, line=line)
    elif len(p) == 7:
        p[0] = DeclarationNode(var_type, name_node, size=ConstantNode(p[4]), line=line)
    else:
        p[0] = [DeclarationNode(var_type, name_node, line=line), AssignmentNode(name_node, p[4], line=line)]

def p_type_specifier(p):
    '''type_specifier : INT_KEYWORD
                      | CHAR_KEYWORD'''
    p[0] = p[1]

def p_assignment_statement(p):
    'assignment_statement : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = AssignmentNode(name=VariableNode(p[1]), value=p[3], line=p.lineno(1))

def p_function_call_statement(p):
    'function_call_statement : IDENTIFIER LPAREN expression_list RPAREN SEMICOLON'
    p[0] = FunctionCallNode(name=VariableNode(p[1]), args=p[3], line=p.lineno(1))

def p_return_statement(p):
    'return_statement : RETURN expression SEMICOLON'
    p[0] = None

def p_expression_list(p):
    '''expression_list : expression
                       | expression_list COMMA expression'''
    if len(p) == 2: p[0] = [p[1]]
    else: p[0] = p[1] + [p[3]]

def p_expression(p):
    '''expression : IDENTIFIER
                  | NUMBER
                  | STRING'''
    slice_type = p.slice[1].type
    if slice_type == 'NUMBER': p[0] = ConstantNode(p[1])
    elif slice_type == 'STRING': p[0] = ConstantNode(p[1])
    else: p[0] = VariableNode(p[1])

def p_error(p):
    if p: print(f"Syntax error at token: {p.type} ('{p.value}') on line {p.lineno}")
    else: print("Syntax error at end of input")

parser = yacc.yacc()
