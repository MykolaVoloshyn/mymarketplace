from django.shortcuts import render, get_object_or_404, redirect
from items.models import Item
from django.contrib.auth.decorators import login_required


@login_required
def owner_stuff(request):
    items = Item.objects.filter(owner=request.user)

    return render(request, 'dashboard/owner_stuff.html', {
        'items': items
    })



