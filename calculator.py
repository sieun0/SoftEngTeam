def main():
    a = int(input())
    while True:
        operator = input()
        if operator == "-" :
            a = sub(a)
        break

def sub(a):
    b = int(input())
    return a - b






if __name__ == "__main__" :
    main()