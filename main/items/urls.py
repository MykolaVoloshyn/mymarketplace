from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('new/', views.new_item, name='new_item'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
    path('', views.searched_items, name='searched_items'),
]