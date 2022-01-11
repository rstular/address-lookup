from enum import Enum


class AddressLookupResultType(Enum):
    """
    Enum for the different types of address verification results
    """

    NOT_FOUND = "notFound"
    HOUSE_NUMBER = "houseNumber"
    STREET = "street"
    LOCALITY = "locality"
    ADMINISTRATIVE_AREA = "administrativeArea"
    PLACE = "place"
    OTHER = "other"


class AddressLookupResult(object):
    """
    Result of the online address lookup
    """

    result_type: AddressLookupResultType
    confidence: float = 0.0
    label: str = None
    country_code: str = None
    country: str = None
    county: str = None
    city: str = None
    district: str = None
    street: str = None
    postal_code: str = None
    house_number: str = None
    type_info: str = None

    def __init__(
        self,
        result_type: AddressLookupResultType,
        confidence: float = None,
        label: str = None,
        country_code: str = None,
        country: str = None,
        county: str = None,
        city: str = None,
        district: str = None,
        street: str = None,
        postal_code: str = None,
        house_number: str = None,
        type_info: str = None,
    ):
        """Initialize the result

        Args:
            result_type (AddressLookupResultType): Type of the result
            confidence (float, optional): Confidence of the result. Defaults to None.
            label (str, optional): Label of the result. Defaults to None.
            country_code (str, optional): ISO 3166-1 Alpha-3 country code of the result. Defaults to None.
            country (str, optional): Country of the result. Defaults to None.
            county (str, optional): County of the result. Defaults to None.
            city (str, optional): City of the result. Defaults to None.
            district (str, optional): District of the result. Defaults to None.
            street (str, optional): Street of the result. Defaults to None.
            postal_code (str, optional): Postal code of the result. Defaults to None.
            house_number (str, optional): House number of the result. Defaults to None.
            type_info (str, optional): Additional information regarding the result type. Defaults to None.
        """
        self.result_type = result_type
        self.confidence = confidence
        self.label = label
        self.country_code = country_code
        self.country = country
        self.county = county
        self.city = city
        self.district = district
        self.street = street
        self.postal_code = postal_code
        self.house_number = house_number
        self.type_info = type_info

    def asdict(self) -> dict:
        """Get the result as a dictionary

        Returns:
            dict: Result as a dictionary
        """
        out_dict = {"result_type": self.result_type.value}
        if self.confidence is not None:
            out_dict["confidence"] = self.confidence
        if self.label is not None:
            out_dict["address"] = {}
            out_dict["address"]["label"] = self.label
            if self.country_code is not None:
                out_dict["address"]["country_code"] = self.country_code
            if self.country is not None:
                out_dict["address"]["country"] = self.country
            if self.county is not None:
                out_dict["address"]["county"] = self.county
            if self.city is not None:
                out_dict["address"]["city"] = self.city
            if self.district is not None:
                out_dict["address"]["district"] = self.district
            if self.street is not None:
                out_dict["address"]["street"] = self.street
            if self.postal_code is not None:
                out_dict["address"]["postal_code"] = self.postal_code
            if self.house_number is not None:
                out_dict["address"]["house_number"] = self.house_number
        if self.type_info is not None:
            out_dict["type_info"] = self.type_info
        return out_dict

    def __str__(self) -> str:
        """Get the result as a string

        Returns:
            str: Result as a string
        """
        return str(self.asdict())
