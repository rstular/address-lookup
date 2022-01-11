# Address Lookup

This package allows you to lookup partial addresses using various online services, returning the address in a standardized form.

## Supported services

 - HERE API (API key required)

### Soon-to-be-supported services

 - Google Maps API

## Obtaining an API key

### HERE API

Create a HERE developer account ([here](https://developer.here.com)). Create a new project, and obtain a REST token. You can use this token with the Address Lookup library.

## Usage

### HERE API

```python
from address_lookup.clients import AddressLookupHereClient

API_KEY = "YOUR_API_KEY"

here_client = AddressLookupHereClient(API_KEY)

result = here_client.lookup_address("White House, USA")
print(result.asdict())
```