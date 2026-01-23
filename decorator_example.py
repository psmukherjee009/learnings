import time
from functools import wraps

def timer(func):
    """A decorator to measure the execution time of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # Record the start time
        result = func(*args, **kwargs)   # Execute the original function
        end_time = time.perf_counter()   # Record the end time
        run_time = end_time - start_time
        print(f"Function {func.__name__!r} took: {run_time:.4f} seconds")
        return result                    # Return the result of the function
    return wrapper

@timer
def long_running_function(seconds):
    """Simulates a task that takes a specified number of seconds."""
    time.sleep(seconds)
    return f"Slept for {seconds} seconds"

# Call the decorated function
result = long_running_function(2)

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
