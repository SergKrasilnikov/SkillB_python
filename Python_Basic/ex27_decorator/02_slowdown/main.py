from typing import Callable, Any
import time

def timer(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        started = time.time()
        result = func(*args, **kwargs)
        endded = time.time()
        sleep_time = 2
        time.sleep(sleep_time)
        print(type(time.sleep(2)))
        runtime = round(endded - started + sleep_time, 10)
        print(f'Run time {runtime}.')
        return result
    return wrapped_func

@timer
def test_one() -> None:
    print('<Normal function in process.>')

@timer
def test_two() -> None:
    print('<Unnormal function in process.>')

first_func = test_one()
second_func = test_two()