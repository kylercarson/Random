from sympy import symbols, Eq, solve

# Define variables
u, y, g1, g2, g3, h1, h2 = symbols('u y g1 g2 g3 h1 h2 ')

# Define an equation
equation = Eq(((g1*g2)*(u-h2*y))/(1+g1*h1) + g3*u-h2*y*g3,y)

# Solve for x
solution = solve(equation, y)
print(solution[0])  # The rearranged equation for x