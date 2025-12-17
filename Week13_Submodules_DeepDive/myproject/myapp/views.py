# from django.shortcuts import render,redirect
# from .forms import DocumentForm
# from django.contrib import messages


# # Create your views here.

# def upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'File uploaded successfully')
#             return redirect('upload')
#         else:
#             messages.error(request, 'File upload failed. Please try again.')
#     else:
#         form = DocumentForm()
#     return render(request, 'upload.html', {'form': form})

# blog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
