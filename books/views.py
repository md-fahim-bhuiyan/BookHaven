from django.shortcuts import render
from .models import Book

def index(request):
    # Fetch the latest added books
    latest_books = Book.objects.order_by('-added_date')[:3]  # Assuming 'published_date' represents the date the book was added
    return render(request, 'index.html', {'latest_books': latest_books})
