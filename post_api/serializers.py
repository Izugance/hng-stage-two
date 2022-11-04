from rest_framework import serializers
from .models import ArithmeticQueryModel


class ArithmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArithmeticQueryModel
        fields = ["operation_type", "x", "y"]