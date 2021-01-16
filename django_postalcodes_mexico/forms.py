# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import PostalCode


class PostalCodeForm(forms.Form):
    postal_code = forms.CharField(label=_('Postal Code'))

    def clean_postal_code(self):
        postal_code = self.cleaned_data['postal_code']
        if not postal_code.isdigit():
            raise ValidationError(
                _("Please enter a valid postal code"), code='invalid', params={'value': postal_code})
        if len(postal_code) != 5:
            raise ValidationError(
                _("A valid postal code must be 5 characters long"), code='invalid', params={'value': postal_code})
        if not PostalCode.objects.filter(d_codigo=postal_code).exists():
            raise ValidationError(
                _("The postal code you entered doesn't exist"), code='invalid', params={'value': postal_code})
        return postal_code
