# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body43(object):
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
        'method': 'str',
        'data': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'method': 'method',
        'data': 'data',
        'is_active': 'is_active'
    }

    def __init__(self, method=None, data=None, is_active=None):  # noqa: E501
        """Body43 - a model defined in Swagger"""  # noqa: E501
        self._method = None
        self._data = None
        self._is_active = None
        self.discriminator = None
        if method is not None:
            self.method = method
        if data is not None:
            self.data = data
        if is_active is not None:
            self.is_active = is_active

    @property
    def method(self):
        """Gets the method of this Body43.  # noqa: E501


        :return: The method of this Body43.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this Body43.


        :param method: The method of this Body43.  # noqa: E501
        :type: str
        """

        self._method = method

    @property
    def data(self):
        """Gets the data of this Body43.  # noqa: E501


        :return: The data of this Body43.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Body43.


        :param data: The data of this Body43.  # noqa: E501
        :type: str
        """

        self._data = data

    @property
    def is_active(self):
        """Gets the is_active of this Body43.  # noqa: E501


        :return: The is_active of this Body43.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Body43.


        :param is_active: The is_active of this Body43.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(Body43, dict):
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
        if not isinstance(other, Body43):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other