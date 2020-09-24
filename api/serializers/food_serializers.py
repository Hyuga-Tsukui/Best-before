from rest_framework import serializers
from foods.models import Food


class FoodSerializer(serializers.ModelSerializer):
    is_dead_line = serializers.BooleanField(read_only=True)
    location = serializers.CharField(read_only=True)

    class Meta:
        model = Food
        fields = ["id", "name", "best_before", "is_dead_line", 'location']
