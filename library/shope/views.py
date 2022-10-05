from atexit import register
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book


def index(request):
    books = Book.objects.order_by('name')
    return render(request,"store/index.html",{'title':'Главная','books':books})


def create(request):
    error=""
    if request.method == 'POST':
        form =BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error="форма не верная"
            
    form = BookForm()
    contaxt = {
        'form':form,
        'error':error
    }
    return render(request,"store/create.html", contaxt)
