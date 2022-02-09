while True:
    password = input('Придумайте пароль: ')
    up_count = low_count = 0

    if len(password) >= 8 and password.isalnum():
        for word_loop in password:
            if word_loop.isupper():
                up_count += 1
            if word_loop.islower():
                low_count += 1
        if up_count != 0 and low_count != 0:
            print('Это надежный пароль!')
            break
        else:
            print('Пароль ненадежен. Попробуйте еще раз.')
    else:
        print('Пароль ненадежен. Попробуйте еще раз.')