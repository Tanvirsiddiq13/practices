def game(string):
    vowels = "AUIOUauioe"
    roki = mehide = 0 
    for i,c in enumerate(string):
        if c in vowels:
            mehide += len(string) - i
        else:
            roki += len(string) - i
    if roki > mehide:
        print(f"roki {roki}")
    elif mehide > roki:
        print(f"mehide {mehide}")
    elif mehide == roki:
        print("Draw")
if __name__ == "__main__":
    s = str(input())
    game(s)