from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.utils.text import slugify
from .forms import ContactoForm
from .models import Contacto

# Create your views here.

class ContactoListView(ListView):
    model = Contacto
    
    def get_queryset(self):
        return Contacto.objects.filter(cliente_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.object_list:
            data['client_title'] = self.object_list[0].cliente
        return data

class ContactoDetailView(DetailView):
    model = Contacto


class ContactoCreate(CreateView):
    model = Contacto
    form_class = ContactoForm

    def get_success_url(self):
        return reverse_lazy('contactos:contactos', args=[self.object.cliente.id, slugify(self.object.cliente.nombre)])

@method_decorator(staff_member_required, name='dispatch')
class ContactoUpdate(UpdateView):
    model = Contacto
    form_class = ContactoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('contactos:update', args=[self.object.id]) + '?ok'

class ContactoDelete(DeleteView):
    model = Contacto

    def get_success_url(self):
        return reverse_lazy('contactos:contactos', args=[self.object.cliente.id, slugify(self.object.cliente.nombre)])