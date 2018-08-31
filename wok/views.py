from django.shortcuts import render
from django.http import HttpResponse
from .models import Panda_Geant
from django.views.generic import  View, CreateView, DeleteView, DetailView, ListView, TemplateView , UpdateView
from django.urls import reverse_lazy
from .forms import PandaForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def index(request):
    
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'wok/index.html')

class PandaCreate (SuccessMessageMixin, CreateView):
    model = Panda_Geant
    form_class = PandaForm
    # success_url = reverse_lazy('games:player-create')
    success_message = "Nouveau Panda créé"
    template_name = 'wok/panda-nouveau.html'
    success_url = reverse_lazy('wok:pandas')

    def get_success_message(self, cleaned_data):
        return self.success_message
    
    # def form_valid(self, form):
        # client = Client.objects.get(pk=self.kwargs['client_id'])
        # print( " ############## TOTO")
        # player = form.save(commit=False)
        # player.user = User
        # player.save()
        # return super().form_valid(form)


class PandaDetail(DetailView):
    model = Panda_Geant
    fields = '__all__'
    template_name = 'wok/panda-detail.html'

    def get_context_data(self, **kwargs):
        context = super(PandaDetail, self).get_context_data(**kwargs)
        context['Panda'] = Panda_Geant.objects.get(pk=self.kwargs['pk'])
        return context

class PandaList(ListView):
    model = Panda_Geant
    fields = '__all__'
    template_name = 'wok/pandas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pandas'] = self.get_queryset()
        return context

class PandaUpdate (UpdateView):
    model = Panda_Geant
    fields = '__all__'
    template_name = 'wok/panda-update.html'
    success_url = reverse_lazy('wok:pandas')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Panda'] = Panda_Geant.objects.get(pk=self.kwargs['pk'])
        return context

    
class PandaDelete (SuccessMessageMixin,DeleteView):
    model = Panda_Geant
    fields = '__all__'
    success_url = reverse_lazy('wok:pandas')
    success_message = "Panda supprimé"
    template_name = 'wok/panda-delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Panda'] = Panda_Geant.objects.get(pk=self.kwargs['pk'])
        return context

    def get_success_message(self, cleaned_data):
        return self.success_message


class PandaTest(View):
    template_name = 'wok/panda-test.html'


def test2(request):
    return render(request, 'wok/test2.html' )
    