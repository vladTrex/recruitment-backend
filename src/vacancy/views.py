from django.shortcuts import render
from rest_framework import generics, mixins
from django.db.models import Q
from .models import Vacancy
from .serializers import VacancySerializer

class VacancyListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer
    # queryset = Vacancy.objects.all()

    def get_queryset(self):
        qs = Vacancy.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(description__icontains=query)).distinct()
        return qs
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class VacancyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = VacancySerializer

    def get_queryset(self):
        return Vacancy.objects.all()



