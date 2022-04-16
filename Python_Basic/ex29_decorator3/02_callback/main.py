import functools

app = {}
route = app.get('//')

def callback(route):
    def decorator(func):

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if route:
                response = route
                print('Ответ:', response)
            else:
                print('Такого пути нет')
            result = func(*args, **kwargs)
            return result
        return wrapped
    return decorator

@callback(route='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

callbackFunc = example()
print(callbackFunc)