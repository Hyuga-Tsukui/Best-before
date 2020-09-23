from django.urls import path

from foods.views import IndexView,  DeadLineListView, CreateFoodView, delete_food, NoDeadLineListView

app_name = 'foods'
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("create/", CreateFoodView.as_view(), name="create"),
    path("<int:food_id>/delete/", delete_food, name="delete"),
    path("dead_line_list/", DeadLineListView.as_view(), name="dead_line_list"),
    path("no_dead_line_list/", NoDeadLineListView.as_view(),
         name="no_dead_line_list"),
]
