from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Yoga Mat',
        'price': 'IDR 100k',
        'desc': 'Pink',
        'cat' : 'yoga'
    }

    return render(request, "main.html", context)