from django.shortcuts import render
from django.http import HttpResponse
from .containers import Franchise


def franchises(request):
    franchise_list = Franchise.objects.all()
    context = {'franchise_list': franchise_list}
    return render(request, 'core/franchises.html', context)
