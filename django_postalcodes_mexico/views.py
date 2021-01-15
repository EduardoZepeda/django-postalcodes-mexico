# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	PostalCode,
)


class PostalCodeCreateView(CreateView):

    model = PostalCode


class PostalCodeDeleteView(DeleteView):

    model = PostalCode


class PostalCodeDetailView(DetailView):

    model = PostalCode


class PostalCodeUpdateView(UpdateView):

    model = PostalCode


class PostalCodeListView(ListView):

    model = PostalCode

