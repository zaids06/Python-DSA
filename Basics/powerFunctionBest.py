def power(x,n):
    if n==0:
        return 1
    small=pow(x,n//2)
    if n%2==0:
        return small*small
    else:
        return (small*small)*x
x = int(input())
n = int(input())
print(pow(x,n))