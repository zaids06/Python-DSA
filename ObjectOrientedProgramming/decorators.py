import time

def execution_time_check(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print("Total time is: ", end_time - start_time)
        return value
    return inner

@execution_time_check
def calc(n):
    tot = 0
    for i in range(1, n+1):
        tot = tot + i
    return tot

print(calc(10000000))
