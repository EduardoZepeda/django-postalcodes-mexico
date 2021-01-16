# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.utils.translation import ugettext_lazy as _

from .models import (
	PostalCode,
)


def getPostalCodeData(request, postal_code):
    postal_codes = PostalCode.objects.filter(d_codigo=postal_code)
    if postal_codes:
        data = {'codigoPostal': postal_code, 
                    'municipio': postal_codes[0].D_mnpio,
                    'estado': postal_codes[0].d_estado,
                    'colonias': list(map(lambda x: x.d_asenta, postal_codes))
                    }
        response = JsonResponse(data)
    response = {"message": _("The")}
    return JsonResponse(response, status=400)