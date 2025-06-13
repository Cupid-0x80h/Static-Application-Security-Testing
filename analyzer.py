# We are importing these classes to check against them
from parser import AssignmentNode, FunctionCallNode

class SecurityAnalyzer:
    def __init__(self):
        self.warnings = []
        self.DANGEROUS_FUNCTIONS = {'gets', 'strcpy', 'strcat', 'sprintf'}
        print("[DEBUG] Analyzer initialized.") # <-- DEBUG PRINT

    def analyze(self, ast):
        if not ast:
            return []
        
        print("[DEBUG] Starting analysis...") # <-- DEBUG PRINT
        
        # Helper to flatten lists of nodes
        def flatten(nodes):
            flat_list = []
            for item in nodes:
                if isinstance(item, list):
                    flat_list.extend(flatten(item))
                elif item:
                    flat_list.append(item)
            return flat_list

        flat_ast = flatten(ast)
            
        for statement in flat_ast:
            # VVV LET'S SEE WHAT THE ANALYZER IS LOOKING AT VVV
            print(f"[DEBUG] Analyzing node: {statement} of type {type(statement)}")
            
            if isinstance(statement, AssignmentNode):
                print("[DEBUG] Node is an AssignmentNode. Visiting...") # <-- DEBUG PRINT
                self.visit_AssignmentNode(statement)
            elif isinstance(statement, FunctionCallNode):
                print("[DEBUG] Node is a FunctionCallNode. Visiting...") # <-- DEBUG PRINT
                self.visit_FunctionCallNode(statement)
        
        print(f"[DEBUG] Analysis complete. Found {len(self.warnings)} warnings.") # <-- DEBUG PRINT
        return self.warnings

    def visit_AssignmentNode(self, node):
        variable_name = node.name.name.lower()
        print(f"[DEBUG] Visiting AssignmentNode. Checking variable: '{variable_name}'") # <-- DEBUG PRINT
        
        if 'password' in variable_name or 'secret' in variable_name or 'key' in variable_name:
            warning_message = (
                f"Line {node.line}: [SECURITY WARNING] "
                f"Hardcoded secret detected in variable '{node.name.name}'."
            )
            self.warnings.append(warning_message)
            print("[DEBUG] ---> Found a hardcoded secret!") # <-- DEBUG PRINT

    def visit_FunctionCallNode(self, node):
        function_name = node.name.name
        print(f"[DEBUG] Visiting FunctionCallNode. Checking function: '{function_name}'") # <-- DEBUG PRINT
        
        if function_name in self.DANGEROUS_FUNCTIONS:
            warning_message = (
                f"Line {node.line}: [CRITICAL WARNING] "
                f"Use of dangerous function '{function_name}' detected. "
                "This can lead to Buffer Overflows."
            )
            self.warnings.append(warning_message)
            print("[DEBUG] ---> Found a dangerous function!") # <-- DEBUG PRINT
