import operator  # Yes, I know, we can use loop or sorted(), but it is shorter way


def collect_stats(file_name):
    count = 0
    result = {}
    text_file = open(file_name, 'r')
    for i_line in text_file:
        for j_char in i_line:
            if j_char != ' ':
                count += 1
            j_char = j_char.lower()
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()
    for key, value in result.items():
        result[key] = round(value / count, 3)

    sorted_tuples = sorted(result.items(), key=operator.itemgetter(1))
    sorted_dict = {key: value for key, value in reversed(sorted_tuples)}

    return sorted_dict


file_name = open('text.txt', 'w')
file_name.write('Mama myla ramu')
file_name.close()

file_name = 'text.txt'
stats = collect_stats(file_name)

file_analysis = open('analysis.txt', 'a')
for key, value in stats.items():
    file_analysis.write(key + ' ' + str(value) + '\n')

file_analysis.close()