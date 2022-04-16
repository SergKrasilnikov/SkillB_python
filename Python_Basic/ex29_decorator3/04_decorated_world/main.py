from typing import Callable

def decorator_with_args_for_any_decorator(decorator_to_enhance: Callable) -> Callable:
    def decorator_maker(*args, **kwargs) -> Callable:
        def decorator_wrapper(func: Callable) -> Callable:
            return decorator_to_enhance(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrapper(text, num):
        print(f'Input args and kwargs in decorater: {args, kwargs}.')
        return func(text, num)
    return wrapper


@decorated_decorator(100, 'money', 200, 'friends')
def decorated_function(text: str, num: int) -> None:
    print('Hello', text, num)



decorated_function("Вселенная и", "всё прочее")

decorated_function('User', 101)