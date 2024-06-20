from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DcForm, DcCoverForm, DcinfoForm
from .models import Dc, DcCover, Dcinfo



class DcList(ListView):
    model = Dc
    template_name = 'dc-index.html.django'
    context_object_name = 'dcs'

class DcDetail(DetailView):
    model = Dc
    template_name = 'dc-detail.html.django'
    context_object_name = 'dc'

class DcCreate(CreateView):
    model = Dc
    template_name = 'add-dc.html.django'
    fields = DcForm.Meta.fields
    success_url = reverse_lazy('dcs-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DcCreate, self).form_valid(form)

class DcUpdate(UpdateView):
    model = Dc
    template_name = 'edit-dc.html.django'
    fields = DcForm.Meta.fields
    success_url = reverse_lazy('dcs-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DcUpdate, self).form_valid(form)

class DcDelete(DeleteView):
    model = Dc
    template_name = 'delete-dc.html.django'
    success_url = reverse_lazy('dcs-home')

class DcCoverCreate(CreateView):
    model = DcCover
    template_name = 'add-dccover.html.django'
    fields = DcCoverForm.Meta.fields
    success_url = reverse_lazy('dcs-home')

    
    
    
    def form_valid(self, form):
        form.instance.dc_id = self.kwargs.get('pk')
        return super(DcCoverCreate, self).form_valid(form)
        
        
class DcinfoCreate(CreateView):
    model = Dcinfo
    template_name = 'add-dcinfo.html.django'
    fields = DcinfoForm.Meta.fields
    success_url = reverse_lazy('dcs-home')

    def form_valid(self, form):
        form.instance.dc_id = self.kwargs.get('pk')
        return super(DcinfoCreate, self).form_valid(form)