def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input())
r=int(input())
print("Factorial of",n,"is",fact(n))
print("Factorial of",r,"is",fact(r))
print("Comination of",r,"is",fact(n)//fact(n-r))
