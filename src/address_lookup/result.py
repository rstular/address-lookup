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

    def get_type(self) -> AddressLookupResultType:
        """Get the type of the result

        Returns:
            AddressLookupResultType: Type of the result
        """
        return self.result_type

    def get_confidence(self) -> float:
        """Get the confidence of the result

        Returns:
            float: Confidence of the result
        """
        return self.confidence

    def get_label(self) -> str:
        """Get the full label of the result

        Returns:
            str: Label of the result
        """
        return self.label

    def get_country_code(self) -> str:
        """Get the ISO 3166-1 Alpha-3 country code of the result

        Returns:
            str: Country code of the result
        """
        return self.country_code

    def get_country(self) -> str:
        """Get the country of the result

        Returns:
            str: Country of the result
        """
        return self.country

    def get_county(self) -> str:
        """Get the county of the result

        Returns:
            str: County of the result
        """
        return self.county

    def get_city(self) -> str:
        """Get the city of the result

        Returns:
            str: City of the result
        """
        return self.city

    def get_district(self) -> str:
        """Get the district of the result

        Returns:
            str: District of the result
        """
        return self.district

    def get_street(self) -> str:
        """Get the street of the result

        Returns:
            str: Street of the result
        """
        return self.street

    def get_postal_code(self) -> str:
        """Get the postal code of the result

        Returns:
            str: Postal code of the result
        """
        return self.postal_code

    def get_house_number(self) -> str:
        """Get the house number of the result

        Returns:
            str: House number of the result
        """
        return self.house_number

    def get_type_info(self) -> str:
        """Get additional type information of the result

        Returns:
            str: Type information of the result
        """
        return self.type_info

    def set_confidence(self, confidence: float):
        """Set the confidence of the result

        Args:
            confidence: Confidence of the result
        """
        self.confidence = confidence

    def set_label(self, label: str):
        """Set the full label of the result

        Args:
            label: Label of the result
        """
        self.label = label

    def set_country_code(self, country_code: str):
        """Set the ISO 3166-1 Alpha-3 country code of the result

        Args:
            country_code: Country code of the result
        """
        self.country_code = country_code

    def set_country(self, country: str):
        """Set the country of the result

        Args:
            country: Country of the result
        """
        self.country = country

    def set_county(self, county: str):
        """Set the county of the result

        Args:
            county: County of the result
        """
        self.county = county

    def set_city(self, city: str):
        """Set the city of the result

        Args:
            city: City of the result
        """
        self.city = city

    def set_district(self, district: str):
        """Set the district of the result

        Args:
            district: District of the result
        """
        self.district = district

    def set_street(self, street: str):
        """Set the street of the result

        Args:
            street: Street of the result
        """
        self.street = street

    def set_postal_code(self, postal_code: str):
        """Set the postal code of the result

        Args:
            postal_code: Postal code of the result
        """
        self.postal_code = postal_code

    def set_house_number(self, house_number: str):
        """Set the house number of the result

        Args:
            house_number: House number of the result
        """
        self.house_number = house_number

    def set_type_info(self, type_info: str):
        """Set additional type information of the result

        Args:
            type_info: Type information of the result
        """
        self.type_info = type_info

    def __str__(self) -> str:
        """Get the result as a string

        Returns:
            str: Result as a string
        """
        return str(self.asdict())
