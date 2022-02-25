def check_error(i_line):
    line = i_line.split()
    if line[1] != '+' and line[1] != '-' and line[1] != '*' and line[1] != '/' and line[1] != '%':
        raise ValueError('Wrong symbol')
    if not line[0].isdigit():
        raise SyntaxError('Wrong operand')
    if line[1] == '/' and line[1] == 0:
        raise ZeroDivisionError('Zero Division Error')

def calculation_func(i_line):
    line = i_line.split()
    if line[1] == '+':
        results = int(line[0]) + int(line[2])
    elif line[1] == '-':
        results = int(line[0]) - int(line[2])
    elif line[1] == '*':
        results = int(line[0]) * int(line[2])
    elif line[1] == '/':
        results = int(line[0]) / int(line[2])
    elif line[1] == '%':
        results = int(line[0]) % int(line[2])
    return results

file = open('calc.txt', 'w')
file.write('100 + 34\n23 / 0\n10 +* 3\n20 -* 2')
file.close()

summ = count = 0

with open('calc.txt', 'r') as file:
    for i_line in file:
        count += 1
        try:
            check_error(i_line)
            results = calculation_func(i_line)
            summ += results
        except (ValueError, SyntaxError, ZeroDivisionError) as err:
            issue_responce = input(f'Equation {i_line}{err} in line {count}. Do you want to solve this issue (yes or no)?')
            if issue_responce == 'yes':
                corrected_line = input('Type correct line: ')
                check_error(corrected_line)
                results = calculation_func(corrected_line)
                summ += results

print('The final result is:', summ)