# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body129(object):
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
        'type': 'str',
        'users': 'list[ApidatabasesUsers]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'users': 'users'
    }

    def __init__(self, name=None, type=None, users=None):  # noqa: E501
        """Body129 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._users = None
        self.discriminator = None
        self.name = name
        if type is not None:
            self.type = type
        self.users = users

    @property
    def name(self):
        """Gets the name of this Body129.  # noqa: E501


        :return: The name of this Body129.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body129.


        :param name: The name of this Body129.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this Body129.  # noqa: E501


        :return: The type of this Body129.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body129.


        :param type: The type of this Body129.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def users(self):
        """Gets the users of this Body129.  # noqa: E501


        :return: The users of this Body129.  # noqa: E501
        :rtype: list[ApidatabasesUsers]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Body129.


        :param users: The users of this Body129.  # noqa: E501
        :type: list[ApidatabasesUsers]
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

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
        if issubclass(Body129, dict):
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
        if not isinstance(other, Body129):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
