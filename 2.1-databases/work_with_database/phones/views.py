from django.shortcuts import render, redirect
from phones.models import Phone

sort_dict = {'name': 'name', 'min_price': 'price', 'max_price': '-price'}

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_type = request.GET.get('sort', 'name')
    template = 'catalog.html'
    context = {
        'phones': Phone.objects.order_by(sort_dict[sort_type]),
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.all()
    for phone in phone_object:
        if phone.slug == slug:
            phone_id_find = phone.id
    template = 'product.html'
    context ={
        'phone': Phone.objects.get(id=phone_id_find),
    }
    return render(request, template, context)
