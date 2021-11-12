# COMMENT превое решение.
def count(a):
    count_letter = not_uniq = 0
    for count_loop in a:
        count_letter += 1
        uniq_letter = 0
        for letter_loop in a:
            if count_loop == letter_loop:
                uniq_letter += 1
                if uniq_letter > 1:
                    not_uniq += 1
                    break
    count_res = count_letter - not_uniq
    return count_res


# COMMENT второе решение
# def count(a):
#     res = 0
#     for word_list in a:
#         index = list(a).count(word_list)
#         if index == 1:
#             res += 1
#
#     return (res)

# COMMENT третье решение
# def count(a):
#     compared_list = []
#     count_res = 0
#     for letter_loop in a:
#         if letter_loop not in compared_list:
#             count_res += 1
#             compared_list.append(letter_loop)
#         else:
#             count_res -= 1
#     return count_res

while True:
    word = input('Введите слово: ')

    results = count(word)

    print('\nКол-во уникальных букв: ', results)
