def infix_to_postfix(expression):
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # Initialize an empty stack and an empty result list
    stack = []
    result = []

    # Remove any spaces from the expression
    expression = expression.replace(" ", "")

    # Iterate over each character in the expression
    for char in expression:
        if char.isalnum():
            # If the character is an operand, add it to the result list
            result.append(char)
        elif char == '(':
            # If the character is an opening parenthesis, push it onto the stack
            stack.append(char)
        elif char == ')':
            # If the character is a closing parenthesis, pop operators from the stack
            # and add them to the result list until an opening parenthesis is encountered
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Remove the opening parenthesis
        else:
            # If the character is an operator, pop operators from the stack
            # and add them to the result list if their precedence is greater
            # or equal to the precedence of the current operator
            while stack and stack[-1] != '(' and precedence[char] <= precedence.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(char)

    # Pop any remaining operators from the stack and add them to the result list
    while stack:
        result.append(stack.pop())

    # Join the result list to form the postfix expression
    return ''.join(result)


# Example usage
infix_expression = "a + b * c - d / e ^ f"
postfix_expression = infix_to_postfix(infix_expression)
print(f"Infix expression: {infix_expression}")
print(f"Postfix expression: {postfix_expression}")
