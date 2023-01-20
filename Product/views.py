from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm, RawForm

# Create your views here.
def get_data(request):
      obj = Product.objects.get(id=1)
      my_products = {
            "title":obj.title,
            "description":obj.description,
            "price":obj.price,
            "summary":obj.summary
      }
      return render(request, "product/details.html", my_products)

def create_new_products(request):
      form = ProductForm(request.POST or None)
      if form.is_valid():
            form.save()
            form.ProductForm()
      my_form = {
           "form":form
      }
      return render (request, "product/create_form.html", my_form)

def raw_form_view(request):
      my_form_2 = RawForm()
      if request.method=="POST":
            my_form_2 = RawForm(request.POST)
            if my_form_2.is_valid():
                  print(my_form_2.cleaned_data)
                  Product.objects.create(**my_form_2.cleaned_data)
            else:
                  print(my_form_2.errors)

      context={
            "form":my_form_2
      }
      return render(request, "product/raw.html", context)

# Lets try and see if we can make the necessary changes
def product_update_view(request):
      obj = Product.objects.get(id=1)
      form = ProductForm(request.POST or None,  instance=obj)
      if form.is_valid():
            form.save()
      context ={
            "form":form
      }
      return render (request, "product/init.html", context)
# dynamic url view
def dynamic_lookup_view(request, my_id):
      obj = get_object_or_404(Product, id=my_id)
      context ={
            "object":obj
      }
      return render(request, "product/dynamic.html", context)
def product_delete_view(request, my_id):
      obj = get_object_or_404(Product, id=my_id)
      if request.method == "POST":
            obj.delete()
      context ={
            "object":obj
      }
      return render(request, "product/dynamic.html", context)

# getting a list of all the products
def product_list_view(request):
      queryset= Product.objects.all()
      context ={
            "object_list":queryset
      }
      return render(request, "product/list.html", context)

