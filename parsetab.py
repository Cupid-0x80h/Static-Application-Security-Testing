
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CHAR_KEYWORD COMMA IDENTIFIER INT_KEYWORD LBRACE LBRACKET LPAREN NUMBER RBRACE RBRACKET RETURN RPAREN SEMICOLON STRINGprogram : statement_liststatement_list : statement_list statementstatement_list : statementstatement : assignment_statement\n| declaration_statement\n| function_call_statement\n| return_statementdeclaration_statement : type_specifier IDENTIFIER SEMICOLON\n| type_specifier IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON\n| type_specifier IDENTIFIER ASSIGN expression SEMICOLONtype_specifier : INT_KEYWORD\n| CHAR_KEYWORDassignment_statement : IDENTIFIER ASSIGN expression SEMICOLONfunction_call_statement : IDENTIFIER LPAREN expression_list RPAREN SEMICOLONreturn_statement : RETURN expression SEMICOLONexpression_list : expression\n| expression_list COMMA expressionexpression : IDENTIFIER\n| NUMBER\n| STRING'
    
_lr_action_items = {'IDENTIFIER':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,24,26,27,28,30,33,36,37,],[8,8,-3,-4,-5,-6,-7,16,18,-11,-12,-2,18,18,-8,18,-15,-13,18,-14,-10,-9,]),'RETURN':([0,2,3,4,5,6,7,13,24,27,28,33,36,37,],[10,10,-3,-4,-5,-6,-7,-2,-8,-15,-13,-14,-10,-9,]),'INT_KEYWORD':([0,2,3,4,5,6,7,13,24,27,28,33,36,37,],[11,11,-3,-4,-5,-6,-7,-2,-8,-15,-13,-14,-10,-9,]),'CHAR_KEYWORD':([0,2,3,4,5,6,7,13,24,27,28,33,36,37,],[12,12,-3,-4,-5,-6,-7,-2,-8,-15,-13,-14,-10,-9,]),'$end':([1,2,3,4,5,6,7,13,24,27,28,33,36,37,],[0,-1,-3,-4,-5,-6,-7,-2,-8,-15,-13,-14,-10,-9,]),'ASSIGN':([8,16,],[14,26,]),'LPAREN':([8,],[15,]),'NUMBER':([10,14,15,25,26,30,],[19,19,19,31,19,19,]),'STRING':([10,14,15,26,30,],[20,20,20,20,20,]),'SEMICOLON':([16,17,18,19,20,21,29,32,35,],[24,27,-18,-19,-20,28,33,36,37,]),'LBRACKET':([16,],[25,]),'RPAREN':([18,19,20,22,23,34,],[-18,-19,-20,29,-16,-17,]),'COMMA':([18,19,20,22,23,34,],[-18,-19,-20,30,-16,-17,]),'RBRACKET':([31,],[35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,],[3,13,]),'assignment_statement':([0,2,],[4,4,]),'declaration_statement':([0,2,],[5,5,]),'function_call_statement':([0,2,],[6,6,]),'return_statement':([0,2,],[7,7,]),'type_specifier':([0,2,],[9,9,]),'expression':([10,14,15,26,30,],[17,21,23,32,34,]),'expression_list':([15,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program_statements','parser.py',34),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',38),
  ('statement_list -> statement','statement_list',1,'p_statement_list_single','parser.py',43),
  ('statement -> assignment_statement','statement',1,'p_statement','parser.py',47),
  ('statement -> declaration_statement','statement',1,'p_statement','parser.py',48),
  ('statement -> function_call_statement','statement',1,'p_statement','parser.py',49),
  ('statement -> return_statement','statement',1,'p_statement','parser.py',50),
  ('declaration_statement -> type_specifier IDENTIFIER SEMICOLON','declaration_statement',3,'p_declaration_statement','parser.py',54),
  ('declaration_statement -> type_specifier IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON','declaration_statement',6,'p_declaration_statement','parser.py',55),
  ('declaration_statement -> type_specifier IDENTIFIER ASSIGN expression SEMICOLON','declaration_statement',5,'p_declaration_statement','parser.py',56),
  ('type_specifier -> INT_KEYWORD','type_specifier',1,'p_type_specifier','parser.py',68),
  ('type_specifier -> CHAR_KEYWORD','type_specifier',1,'p_type_specifier','parser.py',69),
  ('assignment_statement -> IDENTIFIER ASSIGN expression SEMICOLON','assignment_statement',4,'p_assignment_statement','parser.py',73),
  ('function_call_statement -> IDENTIFIER LPAREN expression_list RPAREN SEMICOLON','function_call_statement',5,'p_function_call_statement','parser.py',77),
  ('return_statement -> RETURN expression SEMICOLON','return_statement',3,'p_return_statement','parser.py',81),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser.py',85),
  ('expression_list -> expression_list COMMA expression','expression_list',3,'p_expression_list','parser.py',86),
  ('expression -> IDENTIFIER','expression',1,'p_expression','parser.py',91),
  ('expression -> NUMBER','expression',1,'p_expression','parser.py',92),
  ('expression -> STRING','expression',1,'p_expression','parser.py',93),
]
