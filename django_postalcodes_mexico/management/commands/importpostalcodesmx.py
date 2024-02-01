# -*- coding: utf-8 -*-
import io
import zipfile
from django.core.management.base import BaseCommand, CommandError
import xml.etree.ElementTree as ET

from ...models import PostalCode
from ._utils import (
    get_value_from_node,
    generate_list_of_postalcode_objects,
    get_xml_postal_codes_data,
    parse_xml_postal_codes_file,
)


class Command(BaseCommand):
    help = "Creates a postal code database using the xml data from the Mexican Postal Service (Correos de Mexico)"

    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            "--file",
            nargs="?",
            const="CPdescarga.xml",
            type=str,
            help="Specify the xml file that contains the postal codes",
        )

    def get_function_for_processing_xml_postal_codes(self, xml_file_name):
        if xml_file_name:
            return parse_xml_postal_codes_file(xml_file_name)
        return get_xml_postal_codes_data()

    def handle(self, *args, **options):
        table_already_exist = PostalCode.objects.filter(id=1).exists()
        if table_already_exist:
            self.stdout.write(self.style.WARNING("Postal code table already exists."))
            self.stdout.write(
                self.style.WARNING(
                    "Importing postal codes again could cause data inconsistencies, if you want to import postal codes again please delete the postal code table first."
                )
            )
            return
        try:
            xml_tree = self.get_function_for_processing_xml_postal_codes(
                options["file"]
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    "There was an error obtaining the xml zipped file from Correos de Mexico:"
                    + str(e)
                )
            )
            exit(1)
        PostalCodes = []
        self.stdout.write(
            self.style.WARNING("This process can take a few minutes, please be patient")
        )
        postalCodes = generate_list_of_postalcode_objects(xml_tree)
        self.stdout.write("Creating table...")
        PostalCode.objects.bulk_create([PostalCode(**data) for data in postalCodes])
        self.stdout.write(
            self.style.SUCCESS(
                "The postal code table has been successfully populated"
            )
        )
