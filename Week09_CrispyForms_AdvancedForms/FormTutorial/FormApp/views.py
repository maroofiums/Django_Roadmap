from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

# List all books
class BookListView(ListView):
    model = Book
    template_name = 'FormApp/book_list.html'
    context_object_name = 'books'

# Detail view
class BookDetailView(DetailView):
    model = Book
    template_name = 'FormApp/book_detail.html'

# Create new book
class BookCreateView(CreateView):
    model = Book
    template_name = 'FormApp/book_form.html'
    fields = ['title', 'author', 'published_date']

# Update book
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'FormApp/book_form.html'
    fields = ['title', 'author', 'published_date']

# Delete book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'FormApp/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
