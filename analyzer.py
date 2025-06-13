# We need to know what our AST nodes look like, so we import them.
from parser import AssignmentNode, FunctionCallNode

class SecurityAnalyzer:
    """
    This is our Visitor/Inspector class.
    It walks the AST to find security issues.
    """
    def __init__(self):
        # The list where we'll store our findings.
        self.warnings = []

    def analyze(self, ast):
        """The main method to start the inspection tour."""
        for statement in ast:
            # Check the type of room (node) we are in.
            if isinstance(statement, AssignmentNode):
                # If it's an assignment, use the assignment checklist.
                self.visit_AssignmentNode(statement)

            elif isinstance(statement, FunctionCallNode):
                self.visit_FunctionCallNode(statement)
        return self.warnings

    def visit_AssignmentNode(self, node):
        """
        This is our 'kitchen checklist' for inspecting AssignmentNodes.
        """
        # --- SECURITY CHECK #1: Hardcoded Password ---
        variable_name = node.name.name.lower() # Check name in lowercase

        # The actual security rule:
        if 'password' in variable_name or 'secret' in variable_name or 'key' in variable_name:
            warning_message = (
                f"Line {node.line}: [SECURITY WARNING] "
                f"Hardcoded secret detected in variable '{node.name.name}'."
            )
            self.warnings.append(warning_message)

    def visit_FunctionCallNode(self, node):
        """This is our checklist for inspecting FunctionCallNodes."""
        print(f"DEBUG: Analyzing function call '{node.name.name}' on line {node.line}")
        
        # --- SECURITY CHECK #2: Dangerous Functions ---
        DANGEROUS_FUNCTIONS = {'gets'} # A set of known dangerous functions

        function_name = node.name.name
        if function_name in DANGEROUS_FUNCTIONS:
            warning_message = (
                f"Line {node.line}: [CRITICAL WARNING] "
                f"Use of dangerous function '{function_name}' detected. "
                "This can lead to Buffer Overflows."
            )
            self.warnings.append(warning_message)