# -*- coding: utf-8 -*-
from django.urls import path
from django.views.generic import TemplateView

from . import views


app_name = 'django_postalcodes_mexico'
urlpatterns = [
    # There are postal codes with leading zeros,
    # hence slug is prefered over int
    path(
        '<slug:postal_code>/',
        views.getPostalCodeData,
        name='get-postal-code-data'
        ),
    path(
        'postal-code/<slug:postal_code>/',
        views.getPostalCodeData,
        name='get-postal-code-data-deprecated'
        ),
    path(
        'search/<slug:postal_code>/',
        views.searchSimilarPostalCode,
        name='search-postal-code-data')
]
