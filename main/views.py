from django.shortcuts import render, redirect
from .models import Product


def index_view(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, "index.html", context)


def create_product_view(request):
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        date = request.POST['date']
        photo = request.FILES.get('photo')
        Product.objects.create(
            name=name,
            price=price,
            quantity=quantity,
            date=date,
            photo=photo
        )
        return redirect("index_url")
    return render(request, 'create-product.html')

def search_product_view(request):
    name = request.GET.get('name')
    context = {
        'products': Product.objects.filter(name__icontains=name)
    }
    return render(request, "search-product.html", context)


def update_product_view(request,pk):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        date = request.POST['date']
        photo = request.FILES.get('photo')
        product.name = name
        product.price = price
        product.quantity = quantity
        product.date = date
        if photo is not None:
            product.photo = photo
        product.save()
        return redirect("index_url")
    context = {
        "product" : product
    }
    return render(request, "update-product.html", context)


def delete_product_view(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect("index_url")