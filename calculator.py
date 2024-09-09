import math

class Operation:  #base class for all the operation
    def apply(self, a, b):
        pass

class Add(Operation): #class for addition operation
    def apply(self, a, b):
        return a + b

class Sub(Operation): #class for substraction operation
    def apply(self, a, b):
        return a - b

class Mul(Operation): #class for multiplication operation
    def apply(self, a, b):
        return a * b

class Div(Operation): #class for division operation
    def apply(self, a, b):
        if b == 0:
            raise ValueError("Division by zero!")
        return a / b
    
class Percent(Operation): #class for percentage operation
    def apply(self, a, b):
        return (a * b ) / 100
    

class Pow(Operation): #class for exponentiation operation
    def apply(self, a, b):
        return a ** b
    
class Sin(Operation):
    def apply(self, a, b=None):
        return math.sin(math.radians(a)) # Convert degrees to radians for calculation
    
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
        # Initialize operators and associate them with their respective operation
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
        # Define operator precedence 
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
        #tokenize the input expression
        tokens = self.tokenize(expression)
        print("Tokens:", tokens) # ['2', '+', '3']
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
        for token in tokens: # Iterate over each token in the expression
            if token.isdigit():
                output.append(int(token))   # Append numbers directly to the output
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                            self.precedence.get(token, 0) <= self.precedence.get(operator_stack[-1], 0)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)  # Push opening parentheses onto the stack
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()   # Pop '(' from stack

        # Pop remaining operators from the stack
        while operator_stack:
            output.append(operator_stack.pop())

        return output



    def evaluate_postfix(self, tokens):
        stack = []
        for token in tokens: # Iterate over each token in postfix notation
            if isinstance(token , int):
                stack.append(token)
            elif token in self.operators:
                if token in ['sin','cos','tan','sqrt']: #unary operation
                    a = stack.pop() 
                    result = self.operators[token].apply(a)   
                else:  #binary operation
                    b = stack.pop()
                    a = stack.pop()
                    result = self.operators[token].apply(a, b)
                stack.append(result)  # Push the result back to the stack
        return stack[0] if stack else 0

#create an instance of calculator
cal = Calculator()

#input from the user
expression = input("enter the expression:   ")
print(f"Received expression: {expression}")

result = cal.eval(expression)

print(f"Result: {result}")










 