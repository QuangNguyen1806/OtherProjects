class PostfixCalculator:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expression):
        stack = []
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                stack.append(float(token))
            elif token in self.variables:
                stack.append(float(self.variables[token]))
            elif token in ['+', '-', '*', '/']:
                if len(stack) < 2:
                    return "Error: Insufficient operands for operator {}".format(token)
                else:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                    if token == '+':
                        result = operand1 + operand2
                    elif token == '-':
                        result = operand1 - operand2
                    elif token == '*':
                        result = operand1 * operand2
                    elif token == '/':
                        if operand2 == 0:
                            return "Error: Division by zero"
                        else:
                            result = operand1 / operand2
                    stack.append(result)
            else:
                return "Error: Invalid token {}".format(token)
        if len(stack) == 1:
            return stack[0]
        else:
            return "Error: Invalid expression"

    def process_assignment(self, expression):
        variable_name, arithmetic_expression = expression.split(' = ')
        result = self.evaluate_expression(arithmetic_expression)
        self.variables[variable_name] = result
        return variable_name

    def run(self):
        while True:
            user_input = input("--> ")
            if user_input == "done()":
                break
            elif '=' in user_input:
                result = self.process_assignment(user_input)
                print(result)
            else:
                result = self.evaluate_expression(user_input)
                print(result)


if __name__ == "__main__":
    calculator = PostfixCalculator()
    calculator.run()
