from django.shortcuts import render, get_object_or_404
from .models import Category, Entry, Person, Place
from django.http import HttpResponse
import datetime
from django.http import Http404

# Create your views here.
def welcome_view(request):
    now = datetime.datetime.now()

    html = f"""
    <html>
        <body>
            <h1>Witaj w kronice rodzinnej Święcińskich</h1>
            <p>Aktualna data i czas: {now}</p>
        </body>
    </html>
    """

    return HttpResponse(html)

def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "wpisy/category/list.html",
        {"categories": categories}
    )

def category_detail(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404("Kategoria nie istnieje")

    return render(
        request,
        "wpisy/category/detail.html",
        {"category": category}
    )

def entry_list(request):
    entries = Entry.objects.all()

    return render(
        request,
        "wpisy/entry/list.html",
        {"entries": entries}
    )

def entries_by_category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
    except Category.DoesNotExist:
        raise Http404("Kategoria nie istnieje")

    entries = Entry.objects.filter(category=category).order_by("-event_date")

    return render(
        request,
        "wpisy/entry/by_category.html",
        {
            "category": category,
            "entries": entries,
        }
    )

def entry_detail(request, slug):
    entry = get_object_or_404(Entry, slug=slug)

    return render(
        request,
        "wpisy/entry/detail.html",
        {"entry": entry}
    )
