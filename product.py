from collections import Counter

number_of_shoes = int(input())
shoes_size = Counter(map(int, input().split()))
number_of_costomar = int(input())
income = 0
for _ in range(number_of_costomar):
    size, prices = map(int, input().split())
    if shoes_size[size] > 0:
        income += prices
        shoes_size[size] -= 1
print(income)

