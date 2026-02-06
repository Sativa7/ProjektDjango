from django.contrib import admin
from .models import Category, Person, Place, Entry, Photo

# Register your models here.
admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Place)
#admin.site.register(Entry)
admin.site.register(Photo)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "category", "place")
    list_filter = ("category", "event_date")
    search_fields = ("title", "content")
    filter_horizontal = ("persons",)