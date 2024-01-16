class MyClass:
    def __init__(self):
        pass

    def get_max_value(self,x, y):
        # write you code logic !!
        if x >= y:
            return x
        else:
            return y




# Create an instance of MyClass
x = int(input())
y = int(input())
obj = MyClass()
obj.get_max_value(x, y)
