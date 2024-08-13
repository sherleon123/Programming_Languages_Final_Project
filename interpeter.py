class Interpreter:
    def __init__(self):
        self.functions = {}  # Dictionary to store defined functions

    def define_function(self, name, params, body):
        self.functions[name] = {'params': params, 'body': body}

    def call_function(self, name, args):
        if name not in self.functions:
            raise RuntimeError(f'Error: Function "{name}" is not defined.')
        func = self.functions[name]
        # Here you can implement the evaluation of the function body with provided arguments
        return f'Calling {name} with arguments {args}'
