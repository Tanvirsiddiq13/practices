user_input = int(input())
for i in range(1,user_input+1):
    a = "".join(str(x) for x in range(1,i+1))
    b = "".join(str(x) for x in range(1,i))
    c = b[::-1]
    print(a+c)
   