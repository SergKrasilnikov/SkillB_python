def is_prime(obj):
    if obj < 2:
        return False
    for i in range(2, int(obj**0.5)+1):
        if obj % i == 0:
            return False
    return True

def list_funk(initial_object):
    return [element for index, element in enumerate(initial_object) if is_prime(index)]

# initial_object = 'О Дивный Новый мир!'
# res = list_funk(initial_object)
#
# print(res)
