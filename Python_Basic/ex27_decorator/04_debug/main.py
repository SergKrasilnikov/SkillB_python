from typing import Callable, Any
import functools

def debug(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        result = func(*args, **kwargs)
        print(f'Function name: {func.__name__}{kwargs}.')
        print(f'Function {func.__name__} returned: {result}')
        print(f'{result}\n')
        return result
    return wrapped_func

@debug
def greeting(name, age=None) -> Any:
    if age:
        return f'Hello, {name}! You are {age} old, such a shame!'
    else:
        return f'Hello, {name}!'


greeting(name='Tom')
greeting(name='Bob', age=100)
greeting(name='Kate', age=16)