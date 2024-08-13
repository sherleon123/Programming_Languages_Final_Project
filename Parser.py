class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        functions = []
        while self.pos < len(self.tokens):
            if self.match('DEFUN'):
                functions.append(self.parse_function())
            else:
                # Parse function applications
                functions.append(self.parse_function_application())
        return functions

    def parse_function(self):
        if self.match('DEFUN'):
            func_name = self.consume('IDENT')
            self.consume('LPAREN')
            params = self.parse_params()
            self.consume('RPAREN')
            self.consume('COLON')
            body = self.parse_expression()
            return {'type': 'function', 'name': func_name, 'params': params, 'body': body}
        else:
            raise RuntimeError('Expected function definition')

    def parse_function_application(self):
        if self.match('APPFUN'):
            self.consume('APPFUN')
            self.consume('LPAREN')
            func_name = self.consume('IDENT')  # Function name
            args = []
            while True:
                if self.match('NUMBER') or self.match('IDENT'):
                    args.append(self.consume(self.tokens[self.pos][0]))  # Consume either a number or identifier
                if self.match('COMMA'):
                    self.consume('COMMA')
                else:
                    break
            self.consume('RPAREN')
            return {'type': 'function_application', 'func': func_name, 'args': args}
        else:
            raise RuntimeError('Expected function application')

    def parse_params(self):
        params = []
        while True:
            if self.match('IDENT'):
                params.append(self.consume('IDENT'))
            if self.match('COMMA'):
                self.consume('COMMA')
            else:
                break
        return params

    def parse_expression(self):
        # Here, we'll just support simple expressions like 'x + y' or 'x + 1'
        expr_parts = []
        while self.pos < len(self.tokens) and self.tokens[self.pos][0] not in ('DEFUN', 'APPFUN'):
            expr_parts.append(self.consume(self.tokens[self.pos][0]))
        return ' '.join(expr_parts)

    def match(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == token_type:
            return True
        return False

    def consume(self, token_type):
        if self.match(token_type):
            token = self.tokens[self.pos]
            self.pos += 1
            return token[1]  # Return the value of the token
        raise RuntimeError(f'Expected token type {token_type}')
