# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body143(object):
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
        'username': 'str',
        'password': 'str',
        'type': 'str',
        'databases': 'list[ApidatabaseusersDatabases]'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'type': 'type',
        'databases': 'databases'
    }

    def __init__(self, username=None, password=None, type=None, databases=None):  # noqa: E501
        """Body143 - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._type = None
        self._databases = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if type is not None:
            self.type = type
        if databases is not None:
            self.databases = databases

    @property
    def username(self):
        """Gets the username of this Body143.  # noqa: E501


        :return: The username of this Body143.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Body143.


        :param username: The username of this Body143.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Body143.  # noqa: E501


        :return: The password of this Body143.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Body143.


        :param password: The password of this Body143.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def type(self):
        """Gets the type of this Body143.  # noqa: E501


        :return: The type of this Body143.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body143.


        :param type: The type of this Body143.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def databases(self):
        """Gets the databases of this Body143.  # noqa: E501


        :return: The databases of this Body143.  # noqa: E501
        :rtype: list[ApidatabaseusersDatabases]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this Body143.


        :param databases: The databases of this Body143.  # noqa: E501
        :type: list[ApidatabaseusersDatabases]
        """

        self._databases = databases

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
        if issubclass(Body143, dict):
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
        if not isinstance(other, Body143):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
