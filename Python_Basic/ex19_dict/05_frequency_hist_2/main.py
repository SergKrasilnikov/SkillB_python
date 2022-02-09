def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict

text = input('Введите текст: ').lower()
hist = histogram(text)

for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

invert_dict = dict()

for key in hist:
    search = hist.get(key)
    if invert_dict.get(search) is None:
        invert_dict.update({search : [key]})
    else:
        invert_dict.get(search).append(key)

print('\nИнвертированный словарь частот:')
for i_sym in sorted(invert_dict.keys()):
    print(i_sym, ':', invert_dict[i_sym])