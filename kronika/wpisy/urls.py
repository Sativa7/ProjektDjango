from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome_view),

    path("categories/", views.category_list, name="category_list"),
    path("categories/<slug:slug>/", views.category_detail),

    path("entries/", views.entry_list, name="entry_list"),
    path("categories/<slug:slug>/entries/", views.entries_by_category, name="entries_by_category"),
    path("entries/<slug:slug>/", views.entry_detail, name="entry_detail"),
]
