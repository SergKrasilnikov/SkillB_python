from django.http import HttpResponse
from django.views import View

import random

class ToDoView(View):
    def get(self, request, *args, **kwargs):
        tasks_list = ['Установить python', 'Установить django', 'Запустить сервер', 'Порадоваться результату']
        return HttpResponse(f'<ul><li> {"</li><li>".join(random.sample(tasks_list, 5))} </li></ul>')