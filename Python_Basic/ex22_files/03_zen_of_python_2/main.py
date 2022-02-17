import shutil, os

def histogram(string, sym_dict):
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict


shutil.copy(os.path.abspath(os.path.join('..', '02_zen_of_python//zen.txt')),
            os.path.abspath(os.path.join('..', '03_zen_of_python_2')))  # copy zen.txt file from previous ex

zen_file = open('zen.txt', 'r')

count_letters = count_lines = count_word = 0
spaces = ' '
sym_dict = dict()
for i_line in zen_file:
    count_letters += len(i_line) - i_line.count(spaces)
    count_lines += 1
    count_word += i_line.count(spaces) + 1
    hist = histogram(i_line.lower(), sym_dict)  # count letters for each line

print('Letter count:', str(count_letters))
print('Word count:', str(count_word))
print('Lines count:', str(count_lines))

min = max(hist.values())
for key, value in hist.items():
    if ord(key) >= ord('a') and ord(key) <= ord('z'):  # The ASCII's GOD is here
        if value < min:
            min = value
            min_key = key
            min_value = value

print(f'Rarest letter: {min_key}. It can be found: {min_value} times.')

zen_file.close()