from django.shortcuts import render, redirect, get_object_or_404
from store.form import AddProductForm, AddCategoryForm
from store.models import Product, Category

# Create your views here.
def products(request):
    data= Product.objects.all()
    return render(request, 'store/index.html', {'data': data})

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            new_product = Product.objects.create(**cleaned_data)
            return redirect('product_detail', pk =new_product.pk )
    else:
        form = AddProductForm()
    data = {
        'title': "Add Product",
        'form': form
    }
    return render(request, 'store/add_product_page.html',  data)

def product_detail(request,pk):
    data = get_object_or_404(Product,pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('products')
    return render(request, 'store/product_detail.html', {'data': data})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = AddProductForm(instance=product)
    return render(request, 'store/product_edit.html', {'form': form, 'product': product})

def categories(request):
    data = Category.objects.all()
    return render(request, 'store/categories.html', {'data': data})

def add_category(request):
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Category.objects.create(**cleaned_data)
            return redirect('categories')
    else:
        form = AddCategoryForm()
    data = {
        'title': "Add Category",
        'form': form
    }
    return render(request, 'store/add_category_page.html', data)

def category_detail(request,pk):
    data = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('categories')
    return render(request, 'store/category_detail.html', {'data': data})

def category_edit(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', pk=category.pk)
    else:
        form = AddCategoryForm(instance=category)
    return render(request,'store/category_edit.html', {'form': form, 'category': category})

