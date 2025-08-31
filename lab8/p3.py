import math

def evaluate_functions(x):
    f = math.cos(2 * x)
    f_prime = -2 * math.sin(2 * x)
    f_double_prime = -4 * math.cos(2 * x)
    return f, f_prime, f_double_prime

# Test for x = π
x_value = math.pi
f, f_prime, f_double_prime = evaluate_functions(x_value)

print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")
print(f"f''(x) = {f_double_prime}")
