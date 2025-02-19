if __name__ == '__main__':
        ser = input()
        for s in ser:
            if s.isalnum():
                print(True)
            if s.isalpha():
                print(True)
            if s.isdigit():
                print(True)
            if s.lower():
                print(True)
            if s.upper():
                print(True)
            break
    # little bit update one
    if __name__ == "__main__":
        ser = input()
        print(any(s.isalnum()for s in ser))
        print(any(s.isalpha()for s in ser))
        print(any(s.isdigit()for s in ser))
        print(any(s.lower()for s in ser))
        print(any(s.upper()for s in ser))
    