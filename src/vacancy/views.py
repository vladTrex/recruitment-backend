from django.shortcuts import render
from rest_framework import generics
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyCreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()

class VacancyListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()

class VacancyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()



