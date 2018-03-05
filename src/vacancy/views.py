from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VacancyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()



