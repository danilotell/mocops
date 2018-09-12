from django.urls import path
from .views import ClientesListView, ClienteDetailView, ClienteCreate, ClienteUpdate, ClienteDelete

clientes_patterns = ([
    path('', ClientesListView.as_view(), name='clientes'),
    path('<int:pk>/<slug:slug>/', ClienteDetailView.as_view(), name='cliente'),
    path('create/', ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', ClienteUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ClienteDelete.as_view(), name='delete'),
], 'clientes')