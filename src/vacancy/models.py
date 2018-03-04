from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title
class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title