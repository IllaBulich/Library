from atexit import register
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product,Book
from .forms import BookForm



# def index(request):
#     books = Book.objects.order_by('name')
#     return render(request,"store/index.html",{'title':'Главная','books':books})


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


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'store/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
    
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'store/product/detail.html',
                  {'product': product})