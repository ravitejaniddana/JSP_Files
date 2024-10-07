class CodeGenerator:
    def __init__(self):
        self.output = []
        self.temp_counter = 0

    def generate_temp(self):
        """Generate a new temporary variable."""
        self.temp_counter += 1
        return f't{self.temp_counter}'

    def infix_to_postfix(self, expression):
        """Convert infix expression to postfix using the Shunting Yard algorithm."""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []

        for token in expression.split():
            if token.isalnum():  
                output.append(token)
            elif token in precedence: 
                while (stack and stack[-1] != '(' and
                       precedence[token] <= precedence[stack[-1]]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Pop the '('

        while stack:
            output.append(stack.pop())

        return output

    def generate_code(self, postfix):
        """Generate code from postfix expression."""
        stack = []

        for token in postfix:
            if token.isalnum():  
                stack.append(token)
            else: 
                right_operand = stack.pop()
                left_operand = stack.pop()
                temp_var = self.generate_temp()
                self.output.append(f"{temp_var} = {left_operand} {token} {right_operand}")
                stack.append(temp_var)

    def get_code(self, expression):
        """Main method to generate code from an infix expression."""
        postfix = self.infix_to_postfix(expression)
        self.generate_code(postfix)
        return self.output


if __name__ == "__main__":
    expression = "a + b * c - d"
    code_gen = CodeGenerator()
    generated_code = code_gen.get_code(expression)

    print("Generated Code:")
    for line in generated_code:
        print(line)