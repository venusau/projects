def check_fibonacci(n):
    a = 0
    b = 1
    c=a+b
    while c <= n:
        if n == c:
            return True
        c = a + b
        a = b
        b = c
    return False

def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in l:
        if check_fibonacci(i):
            print(i)

if __name__ == "__main__":
    main()
