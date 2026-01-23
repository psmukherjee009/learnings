# Yield pauses the function and returns. The call next gives the next value.
# For loop automates the next execution
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield 0
    yield from sub_generator() # Delegates to sub_generator
    yield 3

for value in main_generator():
    print(value)
