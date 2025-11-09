"""
puzzle_generator.py — Generates math puzzles of varying difficulty.

Supports:
- Basic arithmetic (+, -, *, /, %, //, **)
- Calculus (integration, differentiation, definite integrals/derivatives)
- Equation solving (linear/quadratic)
Uses SymPy for symbolic math.
"""

import random
import operator
import sympy as sp


class PuzzleGenerator:
    """Class responsible for generating math puzzles of different types."""

    def __init__(self):
        # Define the basic operations available
        self.basic_ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '**': operator.pow,
            '//': operator.floordiv
        }

    # -------------------------------------------------------------------------
    # BASIC ARITHMETIC PUZZLES
    # -------------------------------------------------------------------------
    def _pick_operands(self, level, op):
        """
        Pick numeric operands depending on difficulty level.
        Ensures that division/modulus/floor division never use 0 as the divisor.
        """
        if level == 'Easy':
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        elif level == 'Medium':
            a = random.randint(5, 30)
            b = random.randint(2, 15)
        else:  # Hard
            a = random.randint(10, 100)
            b = random.randint(2, 30)

        # Avoid division/modulus/floor-division by zero
        if op in ('/', '%', '//') and b == 0:
            b = 1
        return a, b

    def _basic_math(self, level):
        """Generate a basic arithmetic problem."""
        op = random.choice(list(self.basic_ops.keys()))
        a, b = self._pick_operands(level, op)
        func = self.basic_ops[op]
        question = f"{a} {op} {b}"
        try:
            answer = func(a, b)
        except Exception:
            answer = 0
        return question, answer

    # -------------------------------------------------------------------------
    # CALCULUS PUZZLES
    # -------------------------------------------------------------------------
    def _integration(self, level):
        """Generate an indefinite integral problem."""
        x = sp.Symbol('x')
        exprs = [x**2, sp.sin(x), sp.exp(x), sp.cos(x), x**3 + 3*x + 2, sp.ln(x)]
        expr = random.choice(exprs)
        if level == 'Hard':
            expr = expr * random.choice([sp.sin(x), sp.exp(x), x])
        question = f"Integrate ∫ {sp.pretty(expr)} dx"
        answer = sp.integrate(expr, x)
        return question, str(answer)

    def _definite_integration(self, level):
        """Generate a definite integral problem."""
        x = sp.Symbol('x')
        expr = random.choice([x**2, sp.sin(x), sp.exp(x), x**3])
        a, b = random.randint(0, 3), random.randint(4, 6)
        question = f"Compute definite integral ∫[{a},{b}] {sp.pretty(expr)} dx"
        answer = sp.integrate(expr, (x, a, b))
        return question, float(answer.evalf())

    def _differentiation(self, level):
        """Generate an indefinite differentiation problem."""
        x = sp.Symbol('x')
        exprs = [x**3, sp.sin(x), sp.exp(x), sp.log(x), x**2 + 3*x + 2]
        expr = random.choice(exprs)
        if level == 'Hard':
            expr = expr * sp.sin(x)
        question = f"Differentiate d/dx({sp.pretty(expr)})"
        answer = sp.diff(expr, x)
        return question, str(answer)

    def _definite_diff(self, level):
        """Generate a problem asking for derivative value at a specific point."""
        x = sp.Symbol('x')
        expr = random.choice([x**3, sp.sin(x), sp.exp(x), x**2 + 2*x])
        val = random.randint(1, 5)
        question = f"Find derivative of {sp.pretty(expr)} at x={val}"
        answer = sp.diff(expr, x).subs(x, val)
        return question, float(answer.evalf())

    # -------------------------------------------------------------------------
    # EQUATION SOLVING PUZZLES
    # -------------------------------------------------------------------------
    def _solve_equation(self, level):
        """Generate an equation-solving problem (linear/quadratic)."""
        x = sp.Symbol('x')

        # Build random equations depending on difficulty
        if level == 'Easy':
            expr = random.randint(1, 5) * x + random.randint(1, 10)
            rhs = random.randint(1, 20)
        elif level == 'Medium':
            expr = random.randint(1, 5) * x**2 + random.randint(1, 5) * x + random.randint(1, 10)
            rhs = random.randint(1, 20)
        else:  # Hard
            expr = random.randint(1, 5) * x**2 + random.randint(1, 5) * x + random.randint(1, 10)
            rhs = random.randint(1, 20)

        question = f"Solve equation: {sp.pretty(expr)} = {rhs}"
        sol = sp.solve(sp.Eq(expr, rhs), x)

        # Safely convert to float if real, otherwise keep as string (complex)
        clean_solutions = []
        for s in sol:
            val = s.evalf()
            if sp.im(val) == 0:  # purely real
                clean_solutions.append(float(val))
            else:
                clean_solutions.append(str(val))

        # If all roots are complex, fallback to a simpler arithmetic problem
        if not clean_solutions:
            return self._basic_math('Medium')

        return question, clean_solutions

    # -------------------------------------------------------------------------
    # MASTER GENERATOR FUNCTION
    # -------------------------------------------------------------------------
    def generate(self, level='Easy'):
        """
        Main entry point.
        Chooses a puzzle type depending on current difficulty level.
        Returns a tuple (question, correct_answer)
        """
        # Weighted categories per difficulty level
        if level == 'Easy':
            categories = ['basic'] * 5 + ['diff', 'solve']
        elif level == 'Medium':
            categories = ['basic'] * 3 + ['int', 'diff', 'solve']
        else:
            categories = ['basic', 'int', 'diff', 'def_int', 'def_diff', 'solve']

        cat = random.choice(categories)

        # Dispatch to the appropriate problem generator
        if cat == 'basic':
            return self._basic_math(level)
        elif cat == 'int':
            return self._integration(level)
        elif cat == 'def_int':
            return self._definite_integration(level)
        elif cat == 'diff':
            return self._differentiation(level)
        elif cat == 'def_diff':
            return self._definite_diff(level)
        elif cat == 'solve':
            return self._solve_equation(level)
        else:
            return "1 + 1", 2
