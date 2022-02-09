friends = int(input('Кол-во друзей: '))
debentur = int(input('Кол-во долговых расписок: '))

friends_money = [0 for i in range(friends)]

for deb_loop in range(debentur):
    print('\n' + str(deb_loop + 1) + ' расписка.')
    whom = int(input('Кому: '))
    who = int(input('От кого: '))
    how = int(input('Сколько: '))
    friends_money[whom - 1] -= how
    friends_money[who - 1] += how

print('\nБаланс:')
for res_loop in range(friends):
    print(str(res_loop + 1) + ' : ' + str(friends_money[res_loop]))

# COMMENT второй способ
# friends_money = [0 for i in range(friends)]
# deb_list = []
# deb = []
#
# for deb_loop in range(debentur):
#     print('\n' + str(deb_loop + 1) + ' расписка.')
#     whom = int(input('Кому: '))
#     who = int(input('От кого: '))
#     how = int(input('Сколько: '))
#
#     deb_list.append([whom, who, how])
#
# for deb_loop in deb_list:
#     friends_money[deb_loop[0] - 1] -= deb_loop[2]
#     friends_money[deb_loop[1] - 1] += deb_loop[2]
#
# print('\nБаланс:')
# for res_loop in range(friends):
#     print(str(res_loop + 1) + ' : ' + str(friends_money[res_loop]))
