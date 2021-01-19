# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from .forms import PostalCodeForm 
from .models import (
	PostalCode,
)
from .utils import generateCityAreasByPostalCode

def getPostalCodeData(request, postal_code):
    postalCodeForm = PostalCodeForm({"postal_code": postal_code})
    if postalCodeForm.is_valid():
        postal_code_data = generateCityAreasByPostalCode(postal_code)
        status=200 if postal_code_data else 404       
        return JsonResponse(postal_code_data, status=status)
    else:
        return JsonResponse(postalCodeForm.errors, status=400)