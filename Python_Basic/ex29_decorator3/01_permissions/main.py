import functools
from collections.abc import Callable

user_permissions = ['admin']

def check_permission(unit=user_permissions[0]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):
            if unit == 'admin':
                result = func(*args, **kwargs)
                return result
            else:
                raise PermissionError(f' Have no permission, to make function {func.__name__}.')
        return wrapped_func
    return decorator

@check_permission('admin')
def delete_site() -> None:
    print('Delete web page.')

@check_permission('user_1')
def add_comment() -> None:
    print('Add comment.')


delete_site()
add_comment()