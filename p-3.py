from itertools import combinations_with_replacement
 
user_input,repeat = input().split()
x = int(repeat)
y = list(user_input)
y.sort()
z = combinations_with_replacement(y,x)
for i in z:
    print("".join(i))