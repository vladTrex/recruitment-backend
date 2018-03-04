from django.conf.urls import url
from django.contrib import admin

from .views import VacancyRetrieveView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', VacancyRetrieveView.as_view(), name='vacancy')
]