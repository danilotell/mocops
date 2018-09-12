from django.urls import path
from .views import ContactoDetailView, ContactoListView, ContactoCreate, ContactoDelete, ContactoUpdate

contactos_patterns = ([
    path('<int:pk>/<slug:slug>/', ContactoListView.as_view(), name='contactos'),
    path('<int:pk>/', ContactoDetailView.as_view(), name='contacto'),
    path('create/', ContactoCreate.as_view(), name='create'),
    path('update/<int:pk>/', ContactoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ContactoDelete.as_view(), name='delete'),
], 'contactos')