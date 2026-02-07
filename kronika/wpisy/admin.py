from django.contrib import admin
from .models import Category, Person, Place, Entry, Photo


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date", "category_with_place")
    list_filter = ("category", "event_date", "created_by", "persons")
    search_fields = ("title", "text")
    filter_horizontal = ("persons",)
    readonly_fields = ("created_at",)

    prepopulated_fields = {"slug": ("title",)}

    @admin.display(description="Kategoria / miejsce")
    def category_with_place(self, obj):
        """
        Bezpieczne wyświetlanie kategorii i miejsca
        (obsługa NULL / None)
        """
        if obj.category and obj.place:
            return f"{obj.category.name} ({obj.place.name})"
        if obj.category:
            return obj.category.name
        return "—"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "entry")
