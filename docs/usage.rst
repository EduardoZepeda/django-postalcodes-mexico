=====
Usage
=====

To use django-postalcodes-mexico in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_postalcodes_mexico.apps.DjangoPostalcodesMexicoConfig',
        ...
    )

Add django-postalcodes-mexico's URL patterns:

.. code-block:: python

    from django_postalcodes_mexico import urls as django_postalcodes_mexico_urls
    from django.urls import path

    urlpatterns = [
        ...
        path('', include(django_postalcodes_mexico_urls)),
        ...
    ]