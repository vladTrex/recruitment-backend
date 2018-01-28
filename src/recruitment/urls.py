from django.conf.urls import url
from django.contrib import admin
from .views import MainApp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MainApp.main_page, name='main_page')
]
