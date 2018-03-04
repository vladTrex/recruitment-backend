from django.shortcuts import render
from rest_framework import generics
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()

class VacancyCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()

