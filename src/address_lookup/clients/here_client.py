import logging

import requests

from .client import AddressLookupClient
from ..errors import AddressLookupException
from ..result import AddressLookupResult, AddressLookupResultType


class AddressLookupHereClient(AddressLookupClient):
    """Client for the HERE Address Lookup API"""

    _url = "https://geocode.search.hereapi.com/v1/geocode"

    def __init__(self, here_api_key: str):
        """
        Initialize the client with the HERE API key.

        Args:
            here_api_key (str): The HERE API key.
        """
        self.api_key = here_api_key

    def lookup_address(self, search_query: str) -> AddressLookupResult:
        """
        Lookup the address using the HERE API.

        Args:
            search_query (str): The address to lookup.

        Returns:
            AddressLookupResult: The result of the address lookup.
        """

        params = {
            "apiKey": self.api_key,
            "q": search_query,
        }
        response = requests.get(self._url, params=params).json()["items"]

        if len(response) == 0:
            return AddressLookupResult(AddressLookupResultType.NOT_FOUND)

        if len(response) > 1:
            logging.warn("More than 1 result found")

        response = response[0]

        try:
            result_type = AddressLookupResultType(response["resultType"])
            if result_type.value + "Type" in response:
                result_info = response[result_type.value + "Type"]
            else:
                result_info = None
        except ValueError:
            result_type = AddressLookupResult.OTHER
            result_info = None
        except KeyError as e:
            raise AddressLookupException(f"Invalid response from HERE API: {str(e)}")

        result = AddressLookupResult(
            result_type,
            type_info=result_info,
        )

        if "scoring" in response and "queryScore" in response["scoring"]:
            result.confidence = response["scoring"]["queryScore"]

        if "address" in response:
            if "label" in response["address"]:
                result.label = response["address"]["label"]
            if "countryCode" in response["address"]:
                result.country_code = response["address"]["countryCode"]
            if "country" in response["address"]:
                result.country = response["address"]["country"]
            if "county" in response["address"]:
                result.county = response["address"]["county"]
            if "city" in response["address"]:
                result.city = response["address"]["city"]
            if "district" in response["address"]:
                result.district = response["address"]["district"]
            if "street" in response["address"]:
                result.street = response["address"]["street"]
            if "postalCode" in response["address"]:
                result.postal_code = response["address"]["postalCode"]
            if "houseNumber" in response["address"]:
                result.house_number = response["address"]["houseNumber"]

        return result
