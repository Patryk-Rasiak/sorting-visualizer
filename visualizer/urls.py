from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bubblesort/', views.bubblesort, name='bubblesort'),
    path('quicksort/', views.quicksort, name='quicksort'),
    path('mergesort/', views.mergesort, name='mergesort'),
    path('selectionsort/', views.selectionsort, name='selectionsort'),
    path('insertionsort/', views.insertionsort, name='insertionsort'),
    path('updatesize/<int:n_bars>/', views.update_size, name='updatesize'),
]
