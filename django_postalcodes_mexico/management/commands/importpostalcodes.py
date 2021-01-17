# -*- coding: utf-8 -*-
import io
import zipfile
from django.core.management.base import BaseCommand, CommandError
import xml.etree.ElementTree as ET

import requests

from ...models import PostalCode
from ._utils import (
    get_value_from_node,
    generate_list_of_postalcode_objects,
    get_xml_postal_codes_data)


class Command(BaseCommand):
    help = 'Creates a postal code database using the data from the official correos de México xml file'

    def handle(self, *args, **options):
        try:
            xml_tree = get_xml_postal_codes_data()
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                'There was an error obtaining the xml zipped file from correos de Mexico:' + str(e)))
            exit(1)
        PostalCodes = []
        self.stdout.write(self.style.WARNING(
            'This process can take a few minutes, please be patient'))
        postalCodes = generate_list_of_postalcode_objects(xml_tree)
        self.stdout.write('Creating database...')
        PostalCode.objects.bulk_create(
            [PostalCode(**data) for data in postalCodes])
        self.stdout.write(self.style.SUCCESS(
            'The postal code database has been successfully populated'))
