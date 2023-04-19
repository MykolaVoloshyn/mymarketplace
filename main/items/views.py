import random

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Item, Category


def searched_items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'items/searched_items.html', {
        'items': items,
        'query': query,
        'category_id': int(category_id),
        'categories': categories
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:4]

    return render(request, 'items/detail.html', {
        'item': item,
        'related_items': related_items
    })


@login_required
def new_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()

            return redirect('item:detail', pk=item.pk)

    form = NewItemForm()

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'New item'
    })


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if item.image:
        item.image.delete()

    item.delete()

    return redirect('dashboard:owner_stuff')


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.pk)

    form = EditItemForm(instance=item)

    return render(request, 'items/form.html', {
        'form': form,
        'title': 'Edit item'
    })
