import datetime
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.urls import reverse


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Food(TimeStamp):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    best_before = models.DateField()
    note = models.TextField(blank=True, max_length=300)

    def __str__(self):
        return self.name + self.best_before.strftime('%Y/%m/%d')

    def is_dead_line(self):
        dead_line = timezone.now() + datetime.timedelta(days=3)
        return dead_line.date() >= self.best_before

    @property
    def dead_line(self):
        return self.is_dead_line

    @property
    def location(self):
        return reverse('foods:delete', args=(self.id,))
