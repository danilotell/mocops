from django.urls import path
from .views import ServicioDetailView, ServicioUpdate

servicios_patterns = ([
    path('<int:pk>/', ServicioDetailView.as_view(), name='servicio'),
    path('update/<int:pk>/', ServicioUpdate.as_view(), name='update'),
], 'servicios')