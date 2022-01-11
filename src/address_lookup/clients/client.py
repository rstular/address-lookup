from ..result import AddressLookupResult


class AddressLookupClient:
    """
    Base class for clients for the Address Lookup.
    If you're developing your own client, use this as the base class.
    """

    def __init__(self, api_key: str = None):
        """
        Initialization routine for the client.

        Args:
            api_key (str, optional): API key for the online service. Defaults to None.
        """
        raise NotImplementedError()

    def parse_response(self, response: dict) -> AddressLookupResult:
        """Parse response returned by the online service into a result object.

        Args:
            response (dict): Response from the online service.

        Raises:
            AddressLookupException: The error that occurred during the lookup.

        Returns:
            AddressLookupResult: The result of the address lookup.
        """
        raise NotImplementedError()

    def lookup_address(self, search_query: str) -> AddressLookupResult:
        """Lookup the address using the online service.

        Args:
            search_query (str): The address to lookup.

        Raises:
            AddressLookupException: The error that occurred during the lookup.

        Returns:
            AddressLookupResult: The result of the address lookup.
        """
        raise NotImplementedError()
