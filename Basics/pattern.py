def print_pattern(n):
    num = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            for j in range(n, 0, -1):
                print(num, end=" ")
                num += 1
        else:
            for j in range(n):
                print(num, end=" ")
                num += 1
        print()
n=int(input())
print_pattern(n)
