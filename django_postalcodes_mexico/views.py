# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from .forms import PostalCodeForm 
from .models import (
	PostalCode,
)


def getPostalCodeData(request, postal_code):
    postalCodeForm = PostalCodeForm({"postal_code": postal_code})
    if postalCodeForm.is_valid():
        postal_codes = PostalCode.objects.filter(d_codigo=postal_code)
        postal_code_data = {'codigoPostal': postal_code, 
                    'municipio': postal_codes[0].D_mnpio,
                    'estado': postal_codes[0].d_estado,
                    'colonias': list(map(lambda x: x.d_asenta, postal_codes))
                    }
        return JsonResponse(postal_code_data)
    else:
        return JsonResponse(postalCodeForm.errors, status=400)