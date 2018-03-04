from rest_framework import serializers
from .models import Vacancy, Category

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'pk',
            'title',
            'description'
        ]
        read_only_fields = ['pk']

    def validate_title(self, value):
        qs = Vacancy.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError("The title must be unique")
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title'
        ]

