from django.conf.urls import url
from django.contrib import admin

from .views import VacancyRetrieveView, VacancyCreateView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', VacancyRetrieveView.as_view(), name='vacancy'),
    url(r'^$', VacancyCreateView.as_view(), name='create-vacancy')
]