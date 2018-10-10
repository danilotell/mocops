from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils.text import slugify
from .forms import ServicioForm
from .models import Servicio

# Create your views here.

class ServicioDetailView(DetailView):
    model = Servicio
    

@method_decorator(staff_member_required, name='dispatch')
class ServicioUpdate(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('servicios:update', args=[self.object.id]) + '?ok'
