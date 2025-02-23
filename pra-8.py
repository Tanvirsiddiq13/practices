def rangoli(n,k=0):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets = alphabets[k:]
    if n == 0:
        return alphabets[0]
    f_design = "-".join(reversed(alphabets[0:n+1]))
    s_design = "-".join(alphabets[1:n+1])
    return "-".join([f_design,s_design])
def print_rangoli(n):
    def row(i):
        print("-" * (2*i),rangoli(n-i-1,i),"-"*(2*i),sep = "")
    for i in reversed(range(n)):
        row(i)
    for i in range(1,n):
        row(i)
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)