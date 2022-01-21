# -*- coding: utf-8 -*-
from .forms import PostalCodeForm
from .models import (
    PostalCode,
)


def generateCityAreasByPostalCode(postal_code):
    postal_codes = PostalCode.objects.filter(d_codigo=postal_code)
    if postal_codes:
        postal_code_data = {
            "codigoPostal": postal_code,
            "municipio": postal_codes[0].D_mnpio,
            "estado": postal_codes[0].d_estado,
            "colonias": list(map(lambda x: x.d_asenta, postal_codes)),
        }
        return postal_code_data
    return dict()


def searchPostalCode(postal_code):
    postal_codes = PostalCode.objects.filter(d_codigo__contains=postal_code).distinct(
        "d_codigo"
    )
    if postal_codes:
        postal_code_list = [postal_code.d_codigo for postal_code in postal_codes]
        return {"postal_codes": postal_code_list}
    return dict()
