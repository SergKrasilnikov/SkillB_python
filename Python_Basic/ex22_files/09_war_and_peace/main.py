import operator, shutil


def collect_stats(file_name):
    result = {}
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    sorted_tuples = sorted(result.items(), key=operator.itemgetter(1))
    sorted_dict = {key: value for key, value in reversed(sorted_tuples)}

    return sorted_dict

shutil.unpack_archive('voyna-i-mir.zip')

file_name = 'voyna-i-mir.txt'
stats = collect_stats(file_name)
print(stats)

file_analysis = open('analysis.txt', 'a', encoding='utf-8')
for key, value in stats.items():
    file_analysis.write(key + ' ' + str(value) + '\n')

file_analysis.close()