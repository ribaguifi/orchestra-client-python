# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ApimailboxesResources(object):
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
        'name': 'str',
        'used': 'float',
        'allocated': 'int',
        'unit': 'str'
    }

    attribute_map = {
        'name': 'name',
        'used': 'used',
        'allocated': 'allocated',
        'unit': 'unit'
    }

    def __init__(self, name=None, used=None, allocated=None, unit=None):  # noqa: E501
        """ApimailboxesResources - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._used = None
        self._allocated = None
        self._unit = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if used is not None:
            self.used = used
        if allocated is not None:
            self.allocated = allocated
        if unit is not None:
            self.unit = unit

    @property
    def name(self):
        """Gets the name of this ApimailboxesResources.  # noqa: E501


        :return: The name of this ApimailboxesResources.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApimailboxesResources.


        :param name: The name of this ApimailboxesResources.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def used(self):
        """Gets the used of this ApimailboxesResources.  # noqa: E501


        :return: The used of this ApimailboxesResources.  # noqa: E501
        :rtype: float
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ApimailboxesResources.


        :param used: The used of this ApimailboxesResources.  # noqa: E501
        :type: float
        """

        self._used = used

    @property
    def allocated(self):
        """Gets the allocated of this ApimailboxesResources.  # noqa: E501


        :return: The allocated of this ApimailboxesResources.  # noqa: E501
        :rtype: int
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this ApimailboxesResources.


        :param allocated: The allocated of this ApimailboxesResources.  # noqa: E501
        :type: int
        """

        self._allocated = allocated

    @property
    def unit(self):
        """Gets the unit of this ApimailboxesResources.  # noqa: E501


        :return: The unit of this ApimailboxesResources.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ApimailboxesResources.


        :param unit: The unit of this ApimailboxesResources.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if issubclass(ApimailboxesResources, dict):
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
        if not isinstance(other, ApimailboxesResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
