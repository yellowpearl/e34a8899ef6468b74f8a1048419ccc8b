from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *
from .tasks import create_plot

import logging

logger = logging.getLogger(__name__)

@login_required
def main(request):
    functions = Function.objects.filter(owner=request.user).order_by('-last_update_time')[:]
    return render(request, 'main.html', {'functions': functions})


@login_required
def add_func(request):
    if request.method == 'POST':
        form = NewFunctionForm(request.POST)
        if form.is_valid():
            form._user = request.user
            func = form.save()
            create_plot.delay(func.pk)
            return HttpResponseRedirect('http://127.0.0.1:8000/main')
    else:
        form = NewFunctionForm()
    return render(request, 'add.html', {'form': form},)
