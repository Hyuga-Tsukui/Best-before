from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Food
from .forms import FoodForm
# Create your views here.


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "foods/index.html"

    def get_queryset(self):
        return  Food.objects.filter(user=self.request.user).order_by('best_before')

class CreateFoodView(LoginRequiredMixin, generic.CreateView):
    template_name = "foods/create_food.html"
    form_class = FoodForm
    model = Food
    success_url = reverse_lazy('foods:index')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(CreateFoodView, self).form_valid(form)

@login_required
def delete_food(request, food_id):
    food = Food.objects.get(pk=food_id)
    food.delete()

    return HttpResponseRedirect(reverse("foods:index"))
