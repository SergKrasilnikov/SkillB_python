while True:
    word = input('Введите слово: ')
    word_list = list(word)
    index = 0
    count = len(word)

    for letter_loop in word_list:
        last_letters = word_list[-1 - index]
        if letter_loop == last_letters:
            index += 1
            if index == count:
                print('Слово является палиндромом.')
        else:
            print('Слово не является палиндромом.')
            break
