def new_generation(fr, to, step):
    class_list = []
    for class_loop in range(fr, to + 1, step):
        class_list.append(class_loop)

    return class_list


first_class = []
second_class = []

first_class.extend(new_generation(160, 176, 2))

second_class.extend(new_generation(162, 180, 3))

first_class.extend(second_class)
first_class.sort()

print(first_class)
