from cmath import phase
user_input = complex(input().strip())
a = user_input.real
b = user_input.imag
print(phase(complex(a,b)))
print(abs(complex(a,b)))