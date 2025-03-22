from collections import OrderedDict
my_set = OrderedDict()
for i in range(int(input())):
    item = input().strip().split()
    my_item, item_price = " ".join(item[:-1]),int(item[-1])
    if my_item in my_set:
        my_set[my_item] += item_price
    else:
        my_set[my_item]  = item_price
for i in (my_set):    
    print(i,my_set[i])

