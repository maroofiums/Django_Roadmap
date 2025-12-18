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
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from .models import Document
from django.conf import settings

def post_list(request):
    posts = Document.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def send_test_email(request):
    send_mail(
        subject='Django Test Email',
        message='This is a test email sent from Django.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['user@example.com'],
        fail_silently=False,
    )

    return HttpResponse("Email sent! Check your console.")