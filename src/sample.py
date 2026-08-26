"""Sample module with intentional style issues — useful to demo the linter bot."""


def add(a,b):
    result=a+b
    return result


def greet( name ):
    message = "Hello, " + name + "!"
    print(message )
    return message


class Calculator:
    def __init__(self,start=0):
        self.value=start

    def add(self,x):
        self.value = self.value+x
        return self.value

    def subtract(self, x):
        self.value=self.value - x
        return self.value
