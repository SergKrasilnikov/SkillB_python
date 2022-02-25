def error_recorder(i_line, error):
    BadLog_file = open('registrations_bad.log', 'a', encoding='utf-8')
    BadLog_file.write(i_line + '\t' + str(error) + '\n')

def check_error(i_line):
    line = i_line.split()
    if line[2] not in line:
        raise IndexError('Fields are not complied.')
    if not line[0].isalpha():
        raise NameError('Wrong name.')
    if '@' not in line[1] or '.' not in line[1]:
        raise SyntaxError('Wrong e-mail.')
    if int(line[2]) < 10 or int(line[2]) > 99:
        raise ValueError('Wrong age.')
    else:
        GoodLog_file = open('registrations_good.log', 'a', encoding='utf-8')
        GoodLog_file.write(i_line)

BadLog_file = open('registrations_bad.log', 'w', encoding='utf-8')
GoodLog_file = open('registrations_good.log', 'w', encoding='utf-8')
BadLog_file.close()
GoodLog_file.close()

with open('registrations.txt', 'r', encoding='utf-8') as registration_file:
    for i_line in registration_file:
        try:
            check_error(i_line)
        except (IndexError, NameError, SyntaxError, ValueError) as err:
            error_recorder(i_line, err)
