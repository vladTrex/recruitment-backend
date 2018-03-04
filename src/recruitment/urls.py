from django.conf.urls import url, include
from django.contrib import admin
from .views import HomePageView, ContactView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name='main_page'),
    url(r'^about/', ContactView.as_view(), name='about_page'),
    url(r'^api/vacancies/', include('vacancy.urls'), name='api-vacancies')
]
