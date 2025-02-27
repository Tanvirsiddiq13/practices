from itertools import product
fisrt_input = map(int,input().split())
second_input = map(int,input().split())
print(*list(product(fisrt_input,second_input)))
