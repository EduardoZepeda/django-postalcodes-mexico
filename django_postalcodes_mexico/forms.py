# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    from django.utils.translation import gettext_lazy as _


class PostalCodeForm(forms.Form):
    postal_code = forms.CharField(label=_("Postal Code"))

    def clean_postal_code(self):
        postal_code = self.cleaned_data["postal_code"]
        if not postal_code.isdigit():
            raise ValidationError(
                _("Please enter a valid postal code, only numbers are allowed"),
                code="invalid",
                params={"value": postal_code},
            )
        if len(postal_code) != 5:
            raise ValidationError(
                _("A valid postal code must be 5 characters long"),
                code="invalid",
                params={"value": postal_code},
            )
        return postal_code


class PostalCodeSearchForm(forms.Form):
    postal_code = forms.CharField(label=_("Postal Code"))

    def clean_postal_code(self):
        postal_code = self.cleaned_data["postal_code"]
        if not postal_code.isdigit():
            raise ValidationError(
                _("Please enter a valid postal code, only numbers are allowed"),
                code="invalid",
                params={"value": postal_code},
            )
        return postal_code
