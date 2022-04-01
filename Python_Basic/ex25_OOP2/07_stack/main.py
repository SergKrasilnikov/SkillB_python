class Stack:
    def __init__(self):
        self.__st = []

    def __str__(self):
        return '; '.join(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()

class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append(f'{str(i_priority)} - {self.task[i_priority]}\n')

        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

manager = TaskManager()
manager.new_task('cleaning', 4)
manager.new_task('washing', 4)
manager.new_task('rest', 1)
manager.new_task('eat', 2)
manager.new_task('homework', 2)
print(manager)