x = int(input())
y = int(input())


def divide(x, y):
    try:
        x/y
    except ZeroDivisionError:
        print("Sorry! You are dividing by zero.")
    else:
        print(x/y)
    finally:
        print("This is always executed")
# write your code logic !!

divide(x, y)
