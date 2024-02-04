a=int(input())
b=int(input())

try:
    print(a//b)
except ZeroDivisionError:
    print("Division not possible")
print("Hey you are doing division")