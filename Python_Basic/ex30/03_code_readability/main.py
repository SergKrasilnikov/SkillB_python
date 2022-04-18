from typing import List

#(1):
num_list1: List[int] = [i_num for i_num in range(2, 1001) if i_num % 2 != 0 and i_num % 3 != 0 or i_num == 2 or i_num == 3]
print(num_list1)

#(2):
num_list2 = []
for i_num in range(2, 1001):
    if i_num % 2 != 0 and i_num % 3 != 0 or i_num == 2 or i_num == 3:
        num_list2.append(i_num)

print(num_list2)