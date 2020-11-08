from celery import shared_task
from .models import Function
import logging
import datetime
import matplotlib.pyplot as plt
import os
import string
from django.conf import settings


logger = logging.getLogger(__name__)
access_symbols = string.digits+"+-*/t()"


def check_formula(f):
    for symbol in f:
        if symbol not in access_symbols:
            raise ValueError("Inappropriate value")


def draw(dt, interval, formula):
    plt.clf()
    time_now = int(round(datetime.datetime.now().timestamp()))
    start_time = time_now - interval * 86400
    formula = formula.split('t')
    xa = []
    ya = []
    for x in range(start_time, time_now, dt * 3600):
        y = eval(str(x).join(formula))
        xa.append(x)
        ya.append(y)
    plt.scatter(xa, ya)
    plt.plot(xa, ya)


def save(name='', fmt='png'):
    pwd = os.getcwd()
    logger.info(pwd)
    img_path = settings.MEDIA_ROOT
    os.chdir(img_path)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    return name


@shared_task
def create_plot(func_pk):
    f = Function.objects.get(pk=func_pk)
    try:
        check_formula(f.formula)
        draw(f.dt, f.interval, f.formula)
        f.img = save(f"{f.owner}-{f.pk}", "png")
        f.img_alt = 'Success'
    except Exception as err:
        f.img_alt = str(err)
        f.img = f"{f.owner}-{f.pk}"
    f.update_time()
    f.save()
    return
