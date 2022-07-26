from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(requst, *args, **kwargs):
    return render(requst, 'advertisement/advertisement_list.html', {})


        # HttpResponse('<ul>'
        #                 '<li>Мастер на час</li>'
        #                 '<li>Купим Ваши органы. Дорого.</li>'
        #                 '<li>Ямобур.</li>'
        #                 '</ul>')