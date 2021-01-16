# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'django_postalcodes_mexico'
urlpatterns = [
    url(
        regex="^postal-code/(?P<postal_code>\d+)/$",
        view=views.getPostalCodeData,
        name='get-postal-code-data',
    )
	]
