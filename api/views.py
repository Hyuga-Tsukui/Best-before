from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from foods.models import Food
from .serializers.food_serializers import FoodSerializer


class FoodList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        foods = Food.objects.filter(
            user=self.request.user).order_by('best_before')
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
