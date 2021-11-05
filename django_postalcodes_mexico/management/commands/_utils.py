# -*- coding: utf-8 -*-
import io
import sys
import zipfile
import xml.etree.ElementTree as ET

import requests

from ...models import PostalCode

node_prefix = '{NewDataSet}'
xml_postal_codes_url = 'https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx'
postal_codes_node_tag = '{NewDataSet}table'
database_columns = ['d_codigo', 'd_asenta', 'D_mnpio', 'd_ciudad', 'd_CP', 'c_estado',
                   'c_oficina', 'c_tipo_asenta', 'c_mnpio', 'id_asenta_cpcons', 'd_zona', 'c_cve_ciudad']


def get_value_from_node(node, value):
    try:
        return node.find(value).text
    except:
        return ""


def generate_list_of_postalcode_objects(root, node_tag=postal_codes_node_tag):
    PostalCodes = []
    for node in root.findall(node_tag):
        data = {column: get_value_from_node(
            node, node_prefix + column) for column in database_columns}
        PostalCodes.append(data)
    return PostalCodes


def fetch_zipped_xml_file(url=xml_postal_codes_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'es-MX,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.correosdemexico.gob.mx',
        'Connection': 'keep-alive',
        'Referer': 'https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    # This data was obtained from the browser after a manual download.
    # Please note that it can change in the future
    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '/wEPDwUINzcwOTQyOTgPZBYCAgEPZBYCAgEPZBYGAgMPDxYCHgRUZXh0BTjDmmx0aW1hIEFjdHVhbGl6YWNpw7NuIGRlIEluZm9ybWFjacOzbjogRW5lcm8gMTYgZGUgMjAyMWRkAgcPEA8WBh4NRGF0YVRleHRGaWVsZAUDRWRvHg5EYXRhVmFsdWVGaWVsZAUFSWRFZG8eC18hRGF0YUJvdW5kZ2QQFSEjLS0tLS0tLS0tLSBUICBvICBkICBvICBzIC0tLS0tLS0tLS0OQWd1YXNjYWxpZW50ZXMPQmFqYSBDYWxpZm9ybmlhE0JhamEgQ2FsaWZvcm5pYSBTdXIIQ2FtcGVjaGUUQ29haHVpbGEgZGUgWmFyYWdvemEGQ29saW1hB0NoaWFwYXMJQ2hpaHVhaHVhEUNpdWRhZCBkZSBNw6l4aWNvB0R1cmFuZ28KR3VhbmFqdWF0bwhHdWVycmVybwdIaWRhbGdvB0phbGlzY28HTcOpeGljbxRNaWNob2Fjw6FuIGRlIE9jYW1wbwdNb3JlbG9zB05heWFyaXQLTnVldm8gTGXDs24GT2F4YWNhBlB1ZWJsYQpRdWVyw6l0YXJvDFF1aW50YW5hIFJvbxBTYW4gTHVpcyBQb3Rvc8OtB1NpbmFsb2EGU29ub3JhB1RhYmFzY28KVGFtYXVsaXBhcwhUbGF4Y2FsYR9WZXJhY3J1eiBkZSBJZ25hY2lvIGRlIGxhIExsYXZlCFl1Y2F0w6FuCVphY2F0ZWNhcxUhAjAwAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyAjEzAjE0AjE1AjE2AjE3AjE4AjE5AjIwAjIxAjIyAjIzAjI0AjI1AjI2AjI3AjI4AjI5AjMwAjMxAjMyFCsDIWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAh0PPCsACwBkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQtidG5EZXNjYXJnYSesavHFx4/PcUhOXn0/O0E5DJnP',
        '__VIEWSTATEGENERATOR': 'BE1A6D2E',
        '__EVENTVALIDATION': '/wEWKAKHgaLWCwLG/OLvBgLWk4iCCgLWk4SCCgLWk4CCCgLWk7yCCgLWk7iCCgLWk7SCCgLWk7CCCgLWk6yCCgLWk+iBCgLWk+SBCgLJk4iCCgLJk4SCCgLJk4CCCgLJk7yCCgLJk7iCCgLJk7SCCgLJk7CCCgLJk6yCCgLJk+iBCgLJk+SBCgLIk4iCCgLIk4SCCgLIk4CCCgLIk7yCCgLIk7iCCgLIk7SCCgLIk7CCCgLIk6yCCgLIk+iBCgLIk+SBCgLLk4iCCgLLk4SCCgLLk4CCCgLL+uTWBALa4Za4AgK+qOyRAQLI56b6CwL1/KjtBRvavCjYcdNppWpaENjjAwloL6cu',
        'cboEdo': '00',
        'rblTipo': 'xml',
        'btnDescarga.x': '48',
        'btnDescarga.y': '2'
    }
    try:
        sys.stdout.write('Trying to connect to Mexican Postal Service (Correos de Mexico)\n')
        response = requests.post(url, headers=headers, data=data)
        sys.stdout.write('Response received\n')
    except Exception as e:
        sys.stderr.write(
            'There was a problem trying to get a response from Mexican Postal Service (Correos de Mexico): \n' + str(e))
    return response.content


def get_xml_postal_codes_data():
    with zipfile.ZipFile(io.BytesIO(fetch_zipped_xml_file())) as zipped_xml_file:
        with zipped_xml_file.open('CPdescarga.xml') as buffered_xml_file:
            try:
                root = ET.parse(buffered_xml_file).getroot()
            except Exception as e:
                sys.stderr.write(
                    'There was a problem parsing the xml data: \n' + str(e))
                exit(1)
    return root


def parse_xml_postal_codes_file(xml_file_name):
    try:
        xml_tree = ET.parse(xml_file_name).getroot()
    except Exception as e:
        sys.stderr.write(
            'There was a problem parsing the xml file, please make sure you downloaded it from Mexican Postal Service \'s official page.\n' + str(e))
        exit(1)
    return xml_tree
