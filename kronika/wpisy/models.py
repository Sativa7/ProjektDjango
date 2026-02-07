from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta: #zmieniamy liczbę mnogą
        verbose_name = "Category"
        verbose_name_plural = "Categories" 
        ordering = ['name']


class Person(models.Model):
    name = models.CharField(max_length=100)
    relation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.city})"


class Entry(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    slug = models.SlugField(unique=True)

    event_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    persons = models.ManyToManyField(Person, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        words = self.text.split()
        preview = " ".join(words[:5])
        if len(words) > 5:
            preview += "..."
        return preview
    
    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ['-created_at']

class Photo(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)