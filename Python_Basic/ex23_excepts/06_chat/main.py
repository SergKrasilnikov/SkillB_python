username = input('Name?')
while True:
    responce = input('Chat log: 1; Type message: 2\n')
    if responce == '1':
        try:
            with open('chat.txt', 'r') as file:
                messages = file.readlines()
                print(''.join(messages))
        except FileNotFoundError:
            print('No data in log.')
    elif responce == '2':
        new_massage = input('Type massage:  ')
        with open('chat.txt', 'a') as file:
            file.write(f'{username} : {new_massage}\n')
    else:
        print('Wrong command.\n')

# зачёт!
