from django.contrib import admin
from .models import Category, Person, Place, Entry, Photo

#admin.site.register(Category)
#admin.site.register(Person)
#admin.site.register(Place)
#admin.site.register(Entry)
admin.site.register(Photo)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "category_with_place")
    list_filter = ("category", "event_date", "created_by", "persons")
    search_fields = ("title", "text")
    filter_horizontal = ("persons",)
    readonly_fields = ("created_at",)

    prepopulated_fields = {"slug": ("title",)}

    def category_with_place(self, obj):
        if obj.place:
            return f"{obj.category.name} ({obj.place.name})"
        return obj.category.name

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name",)

