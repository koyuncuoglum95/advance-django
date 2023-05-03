from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

# List All Schools
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

# Retrieve a School by showing its details
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template = 'advcbvapp/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School
    template = 'advcbvapp/school_form.html'


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("advcbvapp:list")
