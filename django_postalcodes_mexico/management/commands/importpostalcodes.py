# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand, CommandError

from ...models import PostalCode


class Command(BaseCommand):
    help = 'Creates the postal code database from the official correos de México xml file (CPdescarga.xml)'

    def handle(self, *args, **options):
        try:
            root = ET.parse('CPdescarga.xxml').getroot()
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(
                 'A file called CPdescarga.xml must exist at the root of the project'))
            exit(1)

        def get_value_from_node(node, value):
            try:
                return node.find(value).text
            except:
                return ""

        PostalCodes = []
        self.stdout.write(self.style.WARNING(
             'This process can take a few minutes, please be patient'))
        for data in root.findall('{NewDataSet}table'):
            d_codigo = get_value_from_node(data, '{NewDataSet}d_codigo')
            d_asenta = get_value_from_node(data, '{NewDataSet}d_asenta')
            D_mnpio = get_value_from_node(data, '{NewDataSet}D_mnpio')
            d_ciudad = get_value_from_node(data, '{NewDataSet}d_ciudad')
            d_CP = get_value_from_node(data, '{NewDataSet}d_CP')
            c_estado = get_value_from_node(data, '{NewDataSet}c_estado')
            c_oficina = get_value_from_node(data, '{NewDataSet}c_oficina')
            c_tipo_asenta = get_value_from_node(
                data, '{NewDataSet}c_tipo_asenta')
            c_mnpio = get_value_from_node(data, '{NewDataSet}c_mnpio')
            id_asenta_cpcons = get_value_from_node(
                data, '{NewDataSet}id_asenta_cpcons')
            d_zona = get_value_from_node(data, '{NewDataSet}d_zona')
            c_cve_ciudad = get_value_from_node(
                data, '{NewDataSet}c_cve_ciudad')
            PostalCodes.append(PostalCode(d_codigo=d_codigo, d_asenta=d_asenta, D_mnpio=D_mnpio, d_ciudad=d_ciudad, d_CP=d_CP, c_estado=c_estado,
                                          c_oficina=c_oficina, c_tipo_asenta=c_tipo_asenta, c_mnpio=c_mnpio, id_asenta_cpcons=id_asenta_cpcons, d_zona=d_zona, c_cve_ciudad=c_cve_ciudad))
        
        self.stdout.write('Creating database...')
        PostalCode.objects.bulk_create(PostalCodes)

        self.stdout.write(self.style.SUCCESS(
            'The postal code database has been successfully populated'))
