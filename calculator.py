import math

class Operation:
    def apply(self, a, b):
        pass

class Add(Operation):
    def apply(self, a, b):
        return a + b

class Sub(Operation):
    def apply(self, a, b):
        return a - b

class Mul(Operation):
    def apply(self, a, b):
        return a * b

class Div(Operation):
    def apply(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b
    
class Percent(Operation):
    def apply(self, a, b):
        return (a * b ) / 100
    
class Square(Operation):
    def apply(self, a):
        return a ** 2
    
class Pow(Operation):
    def apply(self, a, b):
        return a ** b
    
class Sin(Operation):
    def apply(self, a, b=None):
        return math.sin(math.radians(a)) 
    
class Cos(Operation):
    def apply(self, a, b=None):
        return math.cos(math.radians(a))
    
class Tan(Operation):
    def apply(self, a, b=None):
        return math.tan(math.radians(a))
    
class Sqrt(Operation):
    def apply(self, a, b=None):
        return math.sqrt(math.radians(a))
    

class Calculator:
    def __init__(self):
        self.operators = {
            '+': Add(),
            '-': Sub(),
            '*': Mul(),
            '/': Div(),
            '%': Percent(),
            '^': Pow(),
            'sin':Sin(),
            'cos':Cos(),
            'tan':Tan(),
            'sqrt':Sqrt()
        }
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3,
            'sin': 4,
            'cos': 4,
            'tan': 4,
            'sqrt': 4
        }

    def eval(self, expression):
        tokens = self.tokenize(expression)
        print("Tokens:", tokens)
        tokens = self.eval_with_parentheses(tokens)
        print("Tokens after high precedence:", tokens)
        return self.evaluate_postfix(tokens)

    def tokenize(self, expression):
        import re
        tokens = re.findall(r'(sin|cos|tan|sqrt|\d+|\+|\-|\*|\/|\(|\)|\^|\%)', expression)
        return tokens

    def eval_with_parentheses(self,tokens):
        output =  []
        operator_stack = []
        for token in tokens:
            if token.isdigit():
                output.append(int(token))
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                            self.precedence.get(token, 0) <= self.precedence.get(operator_stack[-1], 0)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  

        while operator_stack:
            output.append(operator_stack.pop())

        return output



    def evaluate_postfix(self, tokens):
        stack = []
        for token in tokens:
            if isinstance(token , int):
                stack.append(token)
            elif token in self.operators:
                if token in ['sin','cos','tan','sqrt']:
                    a = stack.pop() 
                    result = self.operators[token].apply(a)   
                else:  
                    b = stack.pop()
                    a = stack.pop()
                    result = self.operators[token].apply(a, b)
                stack.append(result)
        return stack[0] if stack else 0


cal = Calculator()

expression = input("enter the expression:   ")
# print(f"Received expression: {expression}")

result = cal.eval(expression)

print(f"Result: {result}")










 