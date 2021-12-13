text = 'aaAAbbcaaaA'
count = 1
list_text = []

for place_loop in range(len(text) - 1):
    if text[place_loop] != text[place_loop + 1]:
        list_text.append(text[place_loop])
        list_text.append(count)
        count = 0
    count += 1

list_text.append(text[len(text) - 1])
list_text.append(count)
print(''.join(map(str, list_text)))

# COMMENT Второй способ

# text = 'aaAAbbcaaaA'
# count = 1
# list_text = []
#
# for place_loop in range(len(text) - 1):
#     if place_loop == len(text):
#         list_text.append(text[place_loop])
#         if count > 1:
#             list_text.append(count)
#         else:
#             list_text.append(1)
#     elif text[place_loop] != text[place_loop + 1]:
#         list_text.append(text[place_loop])
#         if count > 1:
#             list_text.append(count)
#         else:
#             list_text.append(1)
#         count = 0
#     count += 1
#
# list_text.append(text[len(text) - 1])
# list_text.append(count)
#
# print(''.join(map(str, list_text)))