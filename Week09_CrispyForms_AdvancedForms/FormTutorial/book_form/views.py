from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Book
from .forms import LoginForm, SignupForm

class BookListView(ListView):
    model = Book
    template_name = "FormApp/book_list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "FormApp/book_detail.html"

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ["title", "author", "published_date"]
    template_name = "FormApp/book_form.html"
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ["title", "author", "published_date"]
    template_name = "FormApp/book_form.html"
    success_url = reverse_lazy("book_list")

    def test_func(self):
        return self.get_object().owner == self.request.user

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = "FormApp/book_confirm_delete.html"
    success_url = reverse_lazy("book_list")

    def test_func(self):
        return self.get_object().owner == self.request.user

class SignUpView(FormView):
    template_name = "FormApp/signup.html"
    form_class = SignupForm
    success_url = reverse_lazy("book_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class LoginView(DjangoLoginView):
    template_name = "FormApp/login.html"
    authentication_form = LoginForm

class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy("login")
