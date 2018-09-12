from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

class ClientesListView(ListView):
    model = Cliente
    paginate_by = 5


class ClienteDetailView(DetailView):
    model = Cliente


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('clientes:clientes')

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('clientes:update', args=[self.object.id]) + '?ok'

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('clientes:clientes')