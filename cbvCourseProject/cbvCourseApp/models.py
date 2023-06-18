from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    instructor = models.CharField(max_length=30)
    rating = models.FloatField(null=True)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
