Examples
========

Using HERE API
**************

First, obtain a REST API token from the `HERE Developer Portal <https://developer.here.com/>`_.

Then, you can use the HERE online API as follows:

.. code-block:: python

    from address_lookup.clients import AddressLookupHereClient

    API_KEY = "YOUR_API_KEY"

    here_client = AddressLookupHereClient(API_KEY)

    result = here_client.lookup_address("White House, USA")
    print(result.asdict())

