from django.urls import path

from foods.views import IndexView, CreateFoodView, delete_food

app_name = 'foods'
urlpatterns = [
  path("", IndexView.as_view(), name="index"),
  path("create/", CreateFoodView.as_view(), name="create"),
  path("<int:food_id>/delete/", delete_food, name="delete"),
]
