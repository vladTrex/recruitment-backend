from django.db import models
from rest_framework import reverse

from .const import NO_CATEGORY_ID

class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    category = models.ForeignKey(Category, default=NO_CATEGORY_ID)

    def __str__(self):
        return self.title
    
    @property
    def category_title(self):
        return str(self.category.title)
    
    # def get_api_url(self):
    #     return reverse('api-vacancies:vacancy', kwargs={'pk': self.pk})