from typing import Callable, Any

def how_are_you(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print('<How are you?>')
        print("<I'll keep you looped: I'm borred. >")
        result = func(*args, **kwargs)
        return result
    return wrapped_func

@how_are_you
def test_one() -> None:
    print('<Normal function in process.>')

@how_are_you
def test_two() -> None:
    print('<Unnormal function in process.>')

first_func = test_one()
second_func = test_two()