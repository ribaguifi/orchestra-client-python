# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body146(object):
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
        'service': 'str',
        'is_active': 'bool',
        'data': 'object',
        'password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'service': 'service',
        'is_active': 'is_active',
        'data': 'data',
        'password': 'password'
    }

    def __init__(self, name=None, service=None, is_active=None, data=None, password=None):  # noqa: E501
        """Body146 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._service = None
        self._is_active = None
        self._data = None
        self._password = None
        self.discriminator = None
        self.name = name
        self.service = service
        if is_active is not None:
            self.is_active = is_active
        if data is not None:
            self.data = data
        if password is not None:
            self.password = password

    @property
    def name(self):
        """Gets the name of this Body146.  # noqa: E501

        Required. 64 characters or fewer. Letters, digits and ./- only.  # noqa: E501

        :return: The name of this Body146.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body146.

        Required. 64 characters or fewer. Letters, digits and ./- only.  # noqa: E501

        :param name: The name of this Body146.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def service(self):
        """Gets the service of this Body146.  # noqa: E501


        :return: The service of this Body146.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Body146.


        :param service: The service of this Body146.  # noqa: E501
        :type: str
        """
        if service is None:
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def is_active(self):
        """Gets the is_active of this Body146.  # noqa: E501

        Designates whether this service should be treated as active.   # noqa: E501

        :return: The is_active of this Body146.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Body146.

        Designates whether this service should be treated as active.   # noqa: E501

        :param is_active: The is_active of this Body146.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def data(self):
        """Gets the data of this Body146.  # noqa: E501


        :return: The data of this Body146.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Body146.


        :param data: The data of this Body146.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def password(self):
        """Gets the password of this Body146.  # noqa: E501


        :return: The password of this Body146.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Body146.


        :param password: The password of this Body146.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(Body146, dict):
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
        if not isinstance(other, Body146):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
