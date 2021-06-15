=============================
django-postalcodes-mexico
=============================

.. image:: https://badge.fury.io/py/django-postalcodes-mexico.svg
    :target: https://badge.fury.io/py/django-postalcodes-mexico

.. image:: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico.svg?branch=master
    :target: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico

.. image:: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico

A Django Package for getting and handling the Mexican Postal Service (Correos de Mexico) postal codes information.

Documentation
-------------

The full documentation is at https://django-postalcodes-mexico.readthedocs.io.

Quickstart
----------

Install django-postalcodes-mexico::

    pip install django-postalcodes-mexico

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_postalcodes_mexico.apps.DjangoPostalcodesMexicoConfig',
        ...
    )

Don't forget to run migrate:

.. code-block:: python

    python manage.py migrate

If the installation was succesful a new command named `importpostalcodes` will be available.

Basic Command usage 
-------------------

If you want to download all postal codes automatically run the following command::

    python manage.py importpostalcodes

This command will attempt to connect to the `Mexican Postal Service website` (Correos de Mexico) and download the public zip file that contains all the postal codes available in xml format, extract them, process them and create the corresponding table in your database.

Local import usage
------------------

Alternatively, you can use the official xml file. Download it from the `Mexican Postal Service website`_. and unzip it

Place the xml file in the same level as your manage.py file and run the following command::

    python manage.py importpostalcodes --file=your_file_name.xml

if you don't specify a file name the default file name from `Mexican Postal Service website` (Correos de Mexico) will be used::

    CPdescarga.xml

Add API urls
------------

Add django-postalcodes-mexico's URL patterns:

.. code-block:: python

    from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls
    from django.urls import path

    urlpatterns = [
        ...
        path('', include(django_postalcodes_mexico_urls)),
        ...
    ]


API Usage
---------

Use the following url to retrieve a postal code

.. code-block:: python

    postal-code/<slug:postal_code>/
    # examples:
    # postal-code/01000/
    # postal-code/02000/

If the request was successful you will receive a response in JSON formatted in this way:

.. code-block:: json

    {
      "municipio": "San Cristóbal de las Casas",
      "estado": "Chiapas",
      "colonias": [
        "La Isla",
        "La Merced",
        "De Mexicanos",
        "San Ramón",
        "1ro de Mayo"
      ],
      "codigoPostal": "29240"
    }

Please note that a Postal Code is associated with only one state(estado) and state area (municipio) but with many city areas (colonias).

Features
--------

* Automatic postal codes table generation
* Local file processing

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _Mexican Postal Service website: https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx