from django.shortcuts import render, redirect
from .models import Books
from .forms import BookForm

# view function for home page declared here
def home(request):
    book_list = Books.objects.all()

    return render(request, 'index.html', {'books': book_list})

# view function for create route declared here
def create(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)

        if book_form.is_valid():
            book_form.save()
            return redirect('/')
    else:
        book_form = BookForm()

        return render(request, 'book_form.html', {'form': book_form})