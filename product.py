from itertools import permutations
string, inte = (input().split())
n = int(inte)
sorted_string = sorted(string)
for x in permutations(sorted_string,n) :
    print("".join(x))
   