from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import MarvelForm, MarvelCoverForm, MarvelinfoForm
from .models import Marvel, MarvelCover, Marvelinfo



class MarvelList(ListView):
    model = Marvel
    template_name = 'marvel-index.html.django'
    context_object_name = 'marvels'

class MarvelDetail(DetailView):
    model = Marvel
    template_name = 'marvel-detail.html.django'
    context_object_name = 'marvel'

class MarvelCreate(CreateView):
    model = Marvel
    template_name = 'add-marvel.html.django'
    fields = MarvelForm.Meta.fields
    success_url = reverse_lazy('marvels-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MarvelCreate, self).form_valid(form)

class MarvelUpdate(UpdateView):
    model = Marvel
    template_name = 'edit-marvel.html.django'
    fields = MarvelForm.Meta.fields
    success_url = reverse_lazy('marvels-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(MarvelUpdate, self).form_valid(form)

class MarvelDelete(DeleteView):
    model = Marvel
    template_name = 'delete-marvel.html.django'
    success_url = reverse_lazy('marvels-home')

class MarvelCoverCreate(CreateView):
    model = MarvelCover
    template_name = 'add-marvelcover.html.django'
    fields = MarvelCoverForm.Meta.fields
    success_url = reverse_lazy('marvels-home')

    
def form_valid(self, form):
    form.instance.marvel_id = self.kwargs.get('pk')
    return super(MarvelCoverCreate, self).form_valid(form)
        
        
class MarvelinfoCreate(CreateView):
    model = Marvelinfo
    template_name = 'add-marvelinfo.html.django'
    fields = MarvelinfoForm.Meta.fields
    success_url = reverse_lazy('marvels-home')

    def form_valid(self, form):
        form.instance.marvel_id = self.kwargs.get('pk')
        return super(MarvelinfoCreate, self).form_valid(form)