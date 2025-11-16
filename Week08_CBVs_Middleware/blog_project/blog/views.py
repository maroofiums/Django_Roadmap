from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, LoginForm, PostForm
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

# base_dir = "blog/"
# class list_post(View):
#     template_name = base_dir+"list_post.html"
#     def get(self, request):
#         posts = Post.objects.all().order_by("-created_at","-updated_at")
#         return render(request,self.template_name,{"posts":posts})

class ListPostView(ListView):
    model = Post
    template_name = "blog/list_post.html"
    context_object_name = "posts"
    ordering = ["-created_at","-updated_at"]

class PostDetailsView(DetailView):
    model = Post
    template_name = "blog/post_details.html"
    context_object_name = "post"

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("list_post")

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm 
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("list_post")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("list_post")
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



            # ------------Login/Signin-----------------#


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "✅ Account created successfully!")
            login(request, user)
            return redirect("list_post")
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = SignUpForm()
    return render(request, "blog/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "🎉 Logged in successfully!")
            return redirect("list_post")
        else:
            messages.error(request, "❌ Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, "blog/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "👋 Logged out successfully.")
    return redirect("login")

