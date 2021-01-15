=============================
django-postalcodes-mexico
=============================

.. image:: https://badge.fury.io/py/django-postalcodes-mexico.svg
    :target: https://badge.fury.io/py/django-postalcodes-mexico

.. image:: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico.svg?branch=master
    :target: https://travis-ci.org/EduardoZepeda/django-postalcodes-mexico

.. image:: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EduardoZepeda/django-postalcodes-mexico

A Django Package for handling Mexico postal codes

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

Add django-postalcodes-mexico's URL patterns:

.. code-block:: python

    from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls


    urlpatterns = [
        ...
        url(r'^', include(django_postalcodes_mexico_urls)),
        ...
    ]

Features
--------

* TODO

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
