from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.owner_stuff, name='owner_stuff')
]
