import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views import View
from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = "foods/index.html"

    def get_queryset(self):
        return Food.objects.filter(user=self.request.user).order_by('best_before')




class DeadLineListView(LoginRequiredMixin, generic.ListView):
    template_name = "foods/index.html"

    def get_queryset(self):
        dead_line = timezone.now() + datetime.timedelta(days=3)
        return Food.objects.filter(user=self.request.user).filter(best_before__lte=dead_line.date()).order_by('best_before')




class NoDeadLineListView(LoginRequiredMixin, generic.ListView):
    template_name = "foods/index.html"

    def get_queryset(self):
        dead_line = timezone.now() + datetime.timedelta(days=3)
        return Food.objects.filter(user=self.request.user).filter(best_before__gt=dead_line.date()).order_by('best_before')




class CreateFoodView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': FoodForm(),
        }
        return render(request, 'foods/create_food.html', context)

    def post(self, request, *args, **kwargs):
        form = FoodForm(request.POST)
        if form.is_valid():
            food = form.save(commit=False)
            food.user = request.user
            food.save()
            return redirect(reverse_lazy('foods:index'))
        return render(request, 'foods/create_food.html', {'form':form})




@login_required
def delete_food(request, food_id):
    food = Food.objects.get(pk=food_id)
    food.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
