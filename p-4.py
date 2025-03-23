from itertools import groupby

user_input = input()
z = groupby(user_input)

for x, y in z:
    c = sum(1 for _ in y)
    print(f"({c}, {x})", end=" ")