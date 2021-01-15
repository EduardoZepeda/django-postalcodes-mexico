# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_postalcodes_mexico'
urlpatterns = [
    url(
        regex="^PostalCode/~create/$",
        view=views.PostalCodeCreateView.as_view(),
        name='PostalCode_create',
    ),
    url(
        regex="^PostalCode/(?P<pk>\d+)/~delete/$",
        view=views.PostalCodeDeleteView.as_view(),
        name='PostalCode_delete',
    ),
    url(
        regex="^PostalCode/(?P<pk>\d+)/$",
        view=views.PostalCodeDetailView.as_view(),
        name='PostalCode_detail',
    ),
    url(
        regex="^PostalCode/(?P<pk>\d+)/~update/$",
        view=views.PostalCodeUpdateView.as_view(),
        name='PostalCode_update',
    ),
    url(
        regex="^PostalCode/$",
        view=views.PostalCodeListView.as_view(),
        name='PostalCode_list',
    ),
	]
