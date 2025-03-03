from django.shortcuts import render
from .models import Books

# view function for home page declared here
def home(request):
    book_list = Books.objects.all()

    return render(request, 'index.html', {'books': book_list})
