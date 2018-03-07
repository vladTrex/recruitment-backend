from rest_framework import serializers
from .models import Vacancy, Category

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = [
            'pk',
            'title',
            'description',
            'category',
            'category_title',
            'added_at'
        ]
        read_only_fields = ['pk', 'added_at']

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


