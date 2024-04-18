from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.book_list, name='book_list'),  # URL for listing all books
    # path('add/', views.add_book, name='add_book'),  # URL for adding a new book
    # path('<int:book_id>/', views.book_detail, name='book_detail'),  # URL for viewing book details
    # path('<int:book_id>/edit/', views.edit_book, name='edit_book'),  # URL for editing a book
    # path('<int:book_id>/delete/', views.delete_book, name='delete_book'),  # URL for deleting a book
]

