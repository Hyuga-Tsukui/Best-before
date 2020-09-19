import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Food

# Create your tests here.

class FoodModelTest(TestCase):
    def test_is_not_deadline(self):

        time =  timezone.now() - datetime.timedelta(days=2)
        not_deadline_food = Food(best_before=time)
        self.assertIs(not_deadline_food.is_dead_line(), False)


    def test_is_deadline(self):

        time =  timezone.now() - datetime.timedelta(days=3)
        not_deadline_food = Food(best_before=time)
        self.assertIs(not_deadline_food.is_dead_line(), True)

