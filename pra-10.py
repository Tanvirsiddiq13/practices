user_input, mate_size = map(int,input().split())
w = "WELCOME"
f = "-"
s = ".|."
width = mate_size
for i in range(user_input//2):
    pattan = s *(2*i+1)
    print((pattan.center(width,f)))
meddle = w.center(width, f)
print(meddle)
for i  in range(user_input//2):
    last_patten = s*(user_input-2-(i*2))
    print(last_patten.center(width,f))