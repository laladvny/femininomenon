import datetime
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from main.models import Employee, Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.forms import CarForm, ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    elif filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        category = request.GET.get("category")
        if category:
            product_list = Product.objects.filter(category=category)
        else:
            product_list = Product.objects.all()

    context = {
        'name': 'Adzradevany Aqiila',
        'class': 'PBP A',
        'npm': '2406410121',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def add_employee(request):
    new_employee = Employee.objects.create(
        name = 'lala',
        age = 21,
        persona = 'chill'
    )

    context = {
        'name':new_employee.name,
        'age':new_employee.age,
        'persona':new_employee.persona
    }

    return render(request, "employee.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': str(product.is_featured),
            'user_username': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(json_data, safe=False)

def show_xml_by_id(request, id):
    try:
        product_item = Product.objects.filter(pk=id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)
    
def show_json_by_id(request, id):
    try:
        product = Product.objects.get(pk=id)
        json_data = {
            'id': str(product.id),
            'name': product.name,
            'price': str(product.price),
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': str(product.is_featured),
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(json_data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
@login_required(login_url='/login')
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        new_product = form.save(commit=False)
        new_product.user = request.user
        new_product.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # AJAX response (fetch)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Your account has been successfully created!',
                    'redirect_url': reverse('main:login')
                })

            # Normal non-AJAX form submission
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')

        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.get_json_data()
                error_messages = " ".join(
                    [f"{field}: {', '.join([err['message'] for err in errs])}"
                     for field, errs in errors.items()]
                )
                return JsonResponse({
                    'success': False,
                    'message': error_messages
                })
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Handle AJAX login (fetch)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                response = JsonResponse({
                'success': True,
                'message': 'Login successful!',
                'redirect_url': reverse("main:show_main")
                })
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response


            # Normal (non-AJAX) redirect
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

        else:
            # If form invalid and it's an AJAX request
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.get_json_data()
                # Convert error dict to readable string
                error_messages = " ".join(
                    [f"{field}: {', '.join([err['message'] for err in errs])}"
                     for field, errs in errors.items()]
                )
                return JsonResponse({
                    'success': False,
                    'message': error_messages
                })
            else:
                return render(request, 'login.html', {'form': form})

    else:
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_car(request):
    form = CarForm(request.POST or None)

    new_car = CarForm.objects.create(
        name = 'avanza',
        brand = 'toyota',
        stock = 300
    )

    if form.is_valid() and request.method == "POST":
        name = form.cleaned_data['name']
        brand = form.cleaned_data['brand']
        stock = form.cleaned_data['stock']
        return redirect('main:show_main')
    
    context = {
        name:new_car.name,
        brand:new_car.brand,
        stock:new_car.stock
    }

    return render(request, "add_car.html", context)

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt # Menonaktifkan CSRF protection untuk request AJAX ini
@require_POST # Memastikan hanya HTTP POST yang diterima
def add_product_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling, mengembalikan 'on' jika dicentang
    user = request.user

    new_product = Product(
        name=name, 
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.user = request.user
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
@require_POST
def edit_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.name = strip_tags(request.POST.get("name"))
    product.price = request.POST.get("price")
    product.description = strip_tags(request.POST.get("description"))
    product.category = request.POST.get("category")
    product.thumbnail = request.POST.get("thumbnail")
    product.is_featured = request.POST.get("is_featured") == 'true'
    product.save()

    return JsonResponse({"success": True, "message": "Product updated successfully"})
    
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return JsonResponse({"success": False, "error": "Product not found"}, status=404)

def get_categories_ajax(request):
    categories = list(Product.objects.values_list('category', flat=True).distinct())
    return JsonResponse(categories, safe=False)