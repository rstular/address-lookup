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

    def parse_response(self, response: dict) -> AddressLookupResult:
        """Parse response returned by the HERE API into a result object.

        Args:
            response (dict): Response from the HERE API

        Raises:
            AddressLookupException: The error that occurred during the lookup.

        Returns:
            AddressLookupResult: The result of the address lookup.
        """

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

    def lookup_address(
        self, search_query: str, error_on_multiple: bool = False
    ) -> AddressLookupResult:
        """Lookup the address using the HERE API.

        Args:
            search_query (str): The address to lookup
            error_on_multiple (bool, optional): Whether to raise an exception if multiple results are found. Defaults to False.

        Raises:
            AddressLookupException: The error that occurred during the lookup.

        Returns:
            AddressLookupResult: The result of the address lookup.
        """

        params = {
            "apiKey": self.api_key,
            "q": search_query,
        }
        response = requests.get(self._url, params=params)

        if response.status_code != 200:
            response_json = response.json()
            if "error" in response_json:
                raise AddressLookupException(
                    f'Error "{response_json["error"]}" ({response.status_code}) from HERE API: {response_json["error_description"]}'
                )
            else:
                raise AddressLookupException(
                    f"Error {response.status_code} from HERE API: {response.text}"
                )

        response_json_items = response.json()["items"]

        if len(response_json_items) == 0:
            return AddressLookupResult(AddressLookupResultType.NOT_FOUND)

        if len(response_json_items) > 1:
            logging.warn("More than 1 result found")
            if error_on_multiple:
                raise AddressLookupException(
                    "Multiple results found, but not allowed to ignore"
                )

        return self.parse_response(response_json_items[0])
