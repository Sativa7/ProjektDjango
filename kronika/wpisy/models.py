from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta: #zmieniamy liczbę mnogą
        verbose_name = "Category"
        verbose_name_plural = "Categories" 


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
    title = models.CharField(max_length=200)
    content = models.TextField()
    event_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True, blank=True)
    persons = models.ManyToManyField(Person, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

class Photo(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True)