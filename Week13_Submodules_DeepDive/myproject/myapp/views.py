from django.shortcuts import render
from .forms import DocumentForm
from django.contrib import messages

# Create your views here.

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document uploaded successfully!')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})

