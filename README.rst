=============================
django-postalcodes-mexico
=============================

Leave a star if you find this package useful.

.. image:: https://badge.fury.io/py/django-postalcodes-mexico.svg
    :target: https://badge.fury.io/py/django-postalcodes-mexico

.. image:: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico.svg?branch=master
    :target: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico

.. image:: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico

A Django Package for getting and handling the Mexican Postal Service (Correos de Mexico) postal codes information.

Please leave a star if you find this package useful.

Compatibility
-------------

* Python (3.8 - 3.10)
* Django (2.2 - 4.1)

Documentation
-------------

The full documentation is at https://django-postalcodes-mexico.readthedocs.io.

Quickstart
----------

If you want to use docker compose scroll down to `quickstart using docker compose`

Install django-postalcodes-mexico::

    pip install django-postalcodes-mexico

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        #...
        'django_postalcodes_mexico.apps.DjangoPostalcodesMexicoConfig',
        #...
    )

Don't forget to run migrate:

.. code-block:: bash

    python manage.py migrate

If the installation was succesful a new command named `importpostalcodesmx` will be available.

Basic Command usage 
-------------------

If you want to download all postal codes automatically run the following command::

    python manage.py importpostalcodesmx

This command will attempt to connect to the `Mexican Postal Service website` (Correos de Mexico) and download the public zip file that contains all the postal codes available in xml format, extract them, process them and create the corresponding table in your database.

Local import usage
------------------

Alternatively, you can use the official xml file. Download it from the `Mexican Postal Service website`_. and unzip it

Place the xml file in the same level as your manage.py file and run the following command::

    python manage.py importpostalcodesmx --file=your_file_name.xml

if you don't specify a file name the default file name from `Mexican Postal Service website` (Correos de Mexico) will be used::

    CPdescarga.xml

Add API urls
------------

Add django-postalcodes-mexico's URL patterns:

.. code-block:: python

    from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls
    from django.urls import path

    urlpatterns = [
        # ...
        path('your-url', include(django_postalcodes_mexico_urls)),
        # ...
    ]

Quickstart using docker compose
-------------------------------

To use docker compose to create an endpoint that returns the postal codes do the following: 


First, clone the project and enter the project directory

.. code-block:: bash

    git clone https://github.com/EduardoZepeda/django-postalcodes-mexico.git
    cd django-postalcodes-mexico/
    
Basic environmental variables need to be declared at the root of the project in a file named `db.env`

.. code-block:: python

    # db.env
    POSTGRES_PASSWORD=your-super-strong-password
    POSTGRES_USER=yourUser
    POSTGRES_DB=yourDatabaseName
    SECRET_KEY=a-very-strong-django-secret-key

Also a variable port, where the endpoint will be available, in your OS, must be placed inside a file named `.env`. I used 8009, but you can use any port you want.

.. code-block:: python

    #.env
    POSTAL_CODES_MX_PORT=8009

Once the latest requirements are fulfilled you're ready to go.

.. code-block:: bash

    docker-compose up

The script will fetch the most recent version of mexican postal codes directly to SEPOMEX (official correos de México website), create the required tables and get up a minimal django server, served using gunicorn.

.. code-block:: bash

    curl 0.0.0.0:8009/29240/

API Usage
---------

Use the following url to retrieve a postal code

.. code-block:: python

    your-url/<slug:postal_code>/
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