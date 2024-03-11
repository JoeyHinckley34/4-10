class MathEquation:
    """
    Represents a mathematical equation with basic arithmetic operations (+, -, *, /).

    Attributes:
        terms: A list of sub-equations or numbers representing the terms of the equation.
    """

    def __init__(self, terms):
        """
        Initializes a MathEquation object.

        Args:
            terms: A list of sub-equations or numbers representing the terms of the equation.
        """

        self.terms = terms

    def evaluate(self):
        """
        Evaluates the equation by recursively evaluating terms and applying operators in the correct order.

        Raises:
            TypeError: If an unsupported type is encountered.
            ZeroDivisionError: If division by zero occurs.
            ValueError: If the expression is invalid (e.g., missing operator between operands).
        """

        operators = ['*', '/']
        non_priority_operators = ['+', '-']

        while len(self.terms) > 1:
            # Find and evaluate priority expressions first
            for i in range(len(self.terms) - 1, -1, -1):  # Iterate backwards to avoid index issues
                term = self.terms[i]
                if isinstance(term, str) and term in operators:
                    if i >= len(self.terms) - 2 or i <= 0:
                        raise ValueError("Invalid expression: missing operand(s) around operator")
                    right = self.terms.pop(i + 1)
                    left = self.terms.pop(i - 1)
                    result = self._apply_operator(left, term, right)
                    self.terms.insert(i - 1, result)
                    break

            # Evaluate non-priority expressions from left to right
            for i in range(len(self.terms) - 1):  # Iterate forwards to avoid index issues
                term = self.terms[i]
                if isinstance(term, str) and term in non_priority_operators:
                    if i >= len(self.terms) - 2 or i <= 0:
                        raise ValueError("Invalid expression: missing operand(s) around operator")
                    right = self.terms.pop(i + 1)
                    left = self.terms.pop(i - 1)
                    result = self._apply_operator(left, term, right)
                    self.terms.insert(i - 1, result)
                    break

        return self.terms[0] if self.terms else 0

    def _apply_operator(self, left, operator, right):
        """
        Applies the given operator to the two operands.
        """

        if operator == "+":
            return left + right
        elif operator == "-":
            return left - right
        elif operator == "*":
            return left * right
        elif operator == "/":
            if right == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right
        else:
            raise TypeError(f"Unsupported operator: {operator}")

    def __str__(self):
        """
        Returns a string representation of the equation in infix notation.
        """

        equation = ""
        for term in self.terms:
            if isinstance(term, MathEquation):
                equation += f"({term})"
            else:
                equation += f"{term}"
            equation += " "

        return equation[:-1]  # Remove trailing space


# Example usage
equation1 = MathEquation([2, "+", 3, "*", 4])
print(equation1.evaluate())  # Output: 14

equation2 = MathEquation([10, "/", 2, "-", 1])
print(equation2.evaluate())  # Output: 4

equation3 = MathEquation([2, "+", MathEquation([3, "*", 4]), "-", 1])
print(equation3.evaluate())  # Output: 13

# Error case - missing operand
# equation4 = MathEquation([2, "/", 2])
# try:
#     print(equation4.evaluate())
# except ValueError as e:
#     print(e)  # Output: Invalid expression: missing operand(s) around operator
