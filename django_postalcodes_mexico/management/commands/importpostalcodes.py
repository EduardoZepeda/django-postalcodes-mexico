# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand, CommandError

from ...models import PostalCode


postal_code_node_tag = '{NewDataSet}table'
prefix = '{NewDataSet}'
databaseColumns = ['d_codigo', 'd_asenta', 'D_mnpio', 'd_ciudad', 'd_CP', 'c_estado', 'c_oficina', 'c_tipo_asenta', 'c_mnpio', 'id_asenta_cpcons', 'd_zona', 'c_cve_ciudad']

def get_value_from_node(node, value):
    try:
        return node.find(value).text
    except:
        return ""

def generate_list_of_postalcode_objects(root, node_tag):
    PostalCodes = []
    for node in root.findall(node_tag):
        data = {column:get_value_from_node(node, prefix + column) for column in databaseColumns}
        PostalCodes.append(data)
    return PostalCodes


class Command(BaseCommand):
    help = 'Creates the postal code database from the official correos de México xml file (CPdescarga.xml)'

    def handle(self, *args, **options):
        try:
            root = ET.parse('CPdescarga.xml').getroot()
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(
                 'A file called CPdescarga.xml must exist at the same level as your manage.py file'))
            exit(1)
        PostalCodes = []
        self.stdout.write(self.style.WARNING(
             'This process can take a few minutes, please be patient'))
        postalCodes = generate_list_of_postalcode_objects(root, postal_code_node_tag)
        self.stdout.write('Creating database...')
        PostalCode.objects.bulk_create([PostalCode(**data) for data in postalCodes])
        self.stdout.write(self.style.SUCCESS(
            'The postal code database has been successfully populated'))
