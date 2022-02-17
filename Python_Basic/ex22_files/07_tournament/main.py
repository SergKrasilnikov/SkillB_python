initial_file = open('first_tour.txt', 'w')
initial_file.write('70\nIvanov Serg 80\nSegeev Petr 92\nPetrov Vasiliy 98\nVasiliev Maxim 78')
initial_file.close()
initial_file = open('first_tour.txt', 'r')

k = int(initial_file.readline())

new_list = []
for line in initial_file:
    new_line = line.split()
    if new_line != [] and int(new_line[-1]) > k:
        new_list.append(new_line)
initial_file.close()

new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()


second_file = open('second_tour.txt', 'w')

count = str(len(new_list))

out_lst = []
n = 1

for i_list in new_list:
    name_sim = str(i_list[0][0]) + '.'
    s_win = str(n) + ') ' + name_sim + ' ' + i_list[1] + ' ' + i_list[-1]
    out_lst.append(s_win)
    n += 1

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    second = '\n'.join(out_lst)
    f_out.write(second)

for order_list in out_lst:
    print(f'{order_list}')