def main():
    a = int(input())
    while True:
        operator = input()
        if operator == "-" :
            a = sub(a)
        elif operator == "+":
            a = add(a)
        break

def sub(a):
    b = int(input())
    return a - b

def add(a):
    b = int(input())
    return a + b






if __name__ == "__main__" :
    main()