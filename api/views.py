from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers.food_serializers import FoodSerializer
from foods.models import Food


class FoodList(APIView):

    def get(self, request, format=None):
        foods = Food.objects.filter(
            user=self.request.user).order_by('best_before')
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
