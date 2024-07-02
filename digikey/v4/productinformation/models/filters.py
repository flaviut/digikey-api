# coding: utf-8

"""
    ProductSearch Api

    ProductSearch Api  # noqa: E501

    OpenAPI spec version: v4
    Contact: dl_Agile_Team_B2B_API@digikey.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Filters(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_in_stock': 'bool',
        'exclude_marketplace': 'bool'
    }

    attribute_map = {
        'is_in_stock': 'IsInStock',
        'exclude_marketplace': 'ExcludeMarketplace'
    }

    def __init__(self, is_in_stock=None, exclude_marketplace=None):  # noqa: E501
        """Filters - a model defined in Swagger"""  # noqa: E501
        self._is_in_stock = None
        self._exclude_marketplace = None
        self.discriminator = None
        if is_in_stock is not None:
            self.is_in_stock = is_in_stock
        if exclude_marketplace is not None:
            self.exclude_marketplace = exclude_marketplace

    @property
    def is_in_stock(self):
        """Gets the is_in_stock of this Filters.  # noqa: E501

        Did we use the “IsInStock” limit?  # noqa: E501

        :return: The is_in_stock of this Filters.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_stock

    @is_in_stock.setter
    def is_in_stock(self, is_in_stock):
        """Sets the is_in_stock of this Filters.

        Did we use the “IsInStock” limit?  # noqa: E501

        :param is_in_stock: The is_in_stock of this Filters.  # noqa: E501
        :type: bool
        """

        self._is_in_stock = is_in_stock

    @property
    def exclude_marketplace(self):
        """Gets the exclude_marketplace of this Filters.  # noqa: E501

        Did we use the “ExcludeMarketplace” limit?  # noqa: E501

        :return: The exclude_marketplace of this Filters.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_marketplace

    @exclude_marketplace.setter
    def exclude_marketplace(self, exclude_marketplace):
        """Sets the exclude_marketplace of this Filters.

        Did we use the “ExcludeMarketplace” limit?  # noqa: E501

        :param exclude_marketplace: The exclude_marketplace of this Filters.  # noqa: E501
        :type: bool
        """

        self._exclude_marketplace = exclude_marketplace

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Filters, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Filters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
