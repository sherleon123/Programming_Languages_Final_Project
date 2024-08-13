import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.tokenize()

    def tokenize(self):
        token_spec = [
            ('NUMBER',   r'-?\d+'),  # Integers
            ('BOOL',     r'(True|False)'),  # Boolean literals
            ('PLUS',     r'\+'),  # Addition
            ('MINUS',    r'-'),  # Subtraction
            ('MUL',      r'\*'),  # Multiplication
            ('DIV',      r'/'),  # Division
            ('MOD',      r'%'),  # Modulo
            ('AND',      r'&&'),  # Boolean AND
            ('OR',       r'\|\|'),  # Boolean OR
            ('NOT',      r'!'),  # Boolean NOT
            ('EQ',       r'=='),  # Equal
            ('NEQ',      r'!='),  # Not equal
            ('GT',       r'>'),  # Greater than
            ('LT',       r'<'),  # Less than
            ('GTE',      r'>='),  # Greater than or equal
            ('LTE',      r'<='),  # Less than or equal
            ('LPAREN',   r'\('),  # Left Parenthesis
            ('RPAREN',   r'\)'),  # Right Parenthesis
            ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_]+'),  # Identifiers (function names, variable names)
            ('DEFUN',    r'Defun'),  # Function definition
            ('APPFUN', r'Appfun'),  # Function application
            ('COLON', r':'),  # Colon for lambda expressions
            ('COMMA', r','),  # Comma for separating parameters
            ('LAMBDA',   r'Lambda'),  # Lambda expression
            ('SKIP',     r'[ \t\n]+'),  # Skip whitespace
            ('MISMATCH', r'.'),  # Any other character
        ]
        token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_spec)
        for match in re.finditer(token_regex, self.code):
            kind = match.lastgroup
            value = match.group()
            if kind == 'NUMBER':
                value = int(value)
            elif kind == 'BOOL':
                value = True if value == 'True' else False
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected character: {value}')
            self.tokens.append((kind, value))

    def __iter__(self):
        yield from self.tokens