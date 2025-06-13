import ply.lex as lex

# List of token names. This is required by PLY.
tokens = (
    'INT_KEYWORD',
    'RETURN',
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'SEMICOLON',
    'ASSIGN',
)

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_ASSIGN = r'='
# The t_ignore rule is defined only ONCE here.
t_ignore = ' \t'  # Ignored characters (spaces and tabs)

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A rule for identifiers and keywords
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for keywords
    if t.value == 'int':
        t.type = 'INT_KEYWORD'
    elif t.value == 'return':
        t.type = 'RETURN'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' on line {t.lexer.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()