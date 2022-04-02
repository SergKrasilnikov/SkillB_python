from typing import Callable, Any

def counter(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        result = func(*args, **kwargs)
        print(f'Function: {func.__name__}, called {wrapped_func.count}')
        return result

    wrapped_func.count = 0
    return wrapped_func

@counter
def reverse_string(string) -> Any:
    return str(string)

print(reverse_string('<Unnormal function in process.>'))
print(reverse_string('<Unnormal function in process.>'))