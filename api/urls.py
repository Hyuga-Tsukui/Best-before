from django.urls import path
from .views import FoodList

app_name = 'api'
urlpatterns = [
    path('foods/', FoodList.as_view(), name='foods'),
]
