thik = int(input())
c = "H"
for s in range(thik):
    print((s*c).rjust(thik-1)+c+(s*c).ljust(thik*s))
for s in range(thik+1):
    print((thik*c).center(thik*2)+(thik*c).center(thik*6))
for s in range((thik+1)//2):
    print((c*thik*5).center(thik*6))
for s in range(thik+1):
    print((thik*c).center(thik*2)+(thik*c).center(thik*6))
for s in range(thik):
    print(((c*(thik-s-1)).rjust(thik)+c+(c*(thik-s-1)).ljust(thik)).rjust(thik*6))