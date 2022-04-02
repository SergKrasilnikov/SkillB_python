from typing import Callable, Any
import datetime, functools

def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        try:
            time_dat = datetime.datetime.now()
            result = func(*args, **kwargs)
            print(f'Function name: {func.__name__}.')
            print(f'Function description: {func.__doc__}\n')
        except BaseException:
            print(f'BaseException raised in "{func.__name__}".')
            with open('function_errors.log', 'a+') as errors_file:
                errors_file.write(f'BaseException raised in "{func.__name__}" in {time_dat} (standard time).\n')
            raise BaseException

        return result
    return wrapped_func

@logging
def test_one() -> None:
    """This function turn over the world."""
    print(360 + 'The world is round')
    print('<Normal function in process.>')

@logging
def test_two() -> None:
    """This function place the world in the stable\
position on three elephants and one blower."""
    # print(360 + 'The world is round')
    print('<Unnormal function in process.>')


errors = open('function_errors.log', 'w')
errors.close()

first_func = test_one()
second_func = test_two()