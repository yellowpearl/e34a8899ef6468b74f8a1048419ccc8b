from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Function(models.Model):
    def img_path(self):
        return f'pictures/user_{self.pk}_img_{self.pk}'

    formula = models.CharField(max_length=64)
    dt = models.IntegerField()
    interval = models.IntegerField()
    img = models.ImageField(upload_to=img_path, height_field=None, width_field=None, max_length=100, default='Error')
    img_alt = models.TextField(default='Wait')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.formula

    def update_time(self):
        self.last_update_time = timezone.now()
        self.save()
        return self.last_update_time
