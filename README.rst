==============
Address Lookup
==============

|docs| |pypi-version|

This package allows you to lookup partial addresses using various online services, returning the address in a standardized form.

Supported services
------------------

 - HERE API (API key required)

Soon-to-be-supported services
*****************************

 - Google Maps API

Obtaining an API key
--------------------

HERE API key
************

Create a HERE developer account `here <https://developer.here.com>`_. Create a new project, and obtain a REST token. You can use this token with the Address Lookup library.

Usage
-----

HERE API usage
**************

.. code-block:: python

    from address_lookup.clients import AddressLookupHereClient

    API_KEY = "YOUR_API_KEY"

    here_client = AddressLookupHereClient(API_KEY)

    result = here_client.lookup_address("White House, USA")
    print(result.asdict())


.. |docs| image:: https://readthedocs.org/projects/docs/badge/?version=latest&style=flat
    :alt: Documentation Status
    :scale: 100%
    :target: https://address-lookup.readthedocs.io/en/latest/

.. |pypi-version| image:: https://img.shields.io/pypi/v/address-lookup
    :alt: Documentation Status
    :scale: 100%
    :target: https://pypi.org/project/address-lookup/
