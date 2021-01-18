=============================
django-postalcodes-mexico
=============================

.. image:: https://badge.fury.io/py/django-postalcodes-mexico.svg
    :target: https://badge.fury.io/py/django-postalcodes-mexico

.. image:: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico.svg?branch=master
    :target: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico

.. image:: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico

A Django Package for handling Mexico postal codes. 

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

If the installation was succesful a new command called `importpostalcodes` will be available.

This command connects to `correos de México` and downloads a zip file that contains all the postal codes available in xml format, extracts them, process them and creates the corresponding table in your database.::

    python manage.py importpostalcodes

Add django-postalcodes-mexico's URL patterns:

.. code-block:: python

    from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls


    urlpatterns = [
        ...
        url(r'^', include(django_postalcodes_mexico_urls)),
        ...
    ]


Usage
-----

You can access the following url to retrieve a postal code

.. code-block:: python

    ^postal-code/(?P<postal_code>\d+)/$

And you will receive a response in JSON with the following format:

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

* Automatically connects, downloads postal codes and creates a table 

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
