from django.urls import path
from .views import *

 

urlpatterns=[

     path('',index, name='index'),  # Handle root URL

    path('items/create/', ItemCreate.as_view(), name='item-create'),

    path('items/', ItemList.as_view(), name='item-list'), 

    path('items/<int:pk>/', EditItem.as_view(), name='item-update'),

     path('ditems/<int:pk>/', ItemDetailView.as_view(), name='detail-item'),
]