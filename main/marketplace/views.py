from django.shortcuts import render, redirect
from items.models import Category, Item
from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request, 'marketplace/index.html', {
        'categories': categories,
        'items': items,
    })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')

    form = SignupForm()

    return render(request, 'marketplace/signup.html', {
        'form': form
    })
