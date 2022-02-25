text = 'Alen\nBen\nJ\nSarah\nJD'
file_name = open('people.txt', 'w')
errors_file = open('errors.log', 'w')
file_name.write(text)
file_name.close()

line_count = sym_sum = 0

with open('people.txt', 'r') as people_file:
    for i_line in people_file:
        try:
            line_count += 1
            i_line.strip()
            if len(i_line) < 3:
                raise TypeError
            sym_sum += len(i_line)
        except TypeError:
            print(f'Length of the line {line_count} is shorter than three symbols.')
            errors_file = open('errors.log', 'a+')
            errors_file.write(f'Length of the line {line_count} is shorter than three symbol.\n')
        except FileNotFoundError:
            print('File not found.')
            errors_file = open('errors.log', 'a+')
            errors_file.write('File not found.\n')

    print('Sum of symbols:', sym_sum)
    errors_file.close()
