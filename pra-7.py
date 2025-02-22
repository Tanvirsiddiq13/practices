def print_formatted(number):
    spaces = len(bin(n))-2
    for i in range(1,n+1):
        decimal = (i)
        octal = oct(i)[2:]
        hex_decimat = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal:>{spaces}} {octal:>{spaces}} {hex_decimat:>{spaces}} {binary:>{spaces}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)