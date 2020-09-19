from django.db import models

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Food(TimeStamp):
    name = models.CharField(max_length=50)
    best_before = models.DateField()

    def __str__(self):
        return self.name + self.best_before
