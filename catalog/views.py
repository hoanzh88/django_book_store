from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Catalog
# from .forms import CreatePostForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

class ListPostView(LoginRequiredMixin, ListView):
  model = Catalog
  def get (self, request, *args, **kwargs):
    template_name = 'catalog/list.html'
    obj = {
      'catalogs': Catalog.objects.all()
      # 'catalog': ''
    }
    return render(request, template_name, obj)