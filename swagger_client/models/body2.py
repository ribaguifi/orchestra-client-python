# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body2(object):
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
        'type': 'str',
        'language': 'str',
        'short_name': 'str',
        'full_name': 'str',
        'date_joined': 'datetime',
        'last_login': 'datetime',
        'is_active': 'bool',
        'billcontact': 'ApiaccountsBillcontact'
    }

    attribute_map = {
        'username': 'username',
        'type': 'type',
        'language': 'language',
        'short_name': 'short_name',
        'full_name': 'full_name',
        'date_joined': 'date_joined',
        'last_login': 'last_login',
        'is_active': 'is_active',
        'billcontact': 'billcontact'
    }

    def __init__(self, username=None, type=None, language=None, short_name=None, full_name=None, date_joined=None, last_login=None, is_active=None, billcontact=None):  # noqa: E501
        """Body2 - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._type = None
        self._language = None
        self._short_name = None
        self._full_name = None
        self._date_joined = None
        self._last_login = None
        self._is_active = None
        self._billcontact = None
        self.discriminator = None
        self.username = username
        if type is not None:
            self.type = type
        if language is not None:
            self.language = language
        if short_name is not None:
            self.short_name = short_name
        self.full_name = full_name
        if date_joined is not None:
            self.date_joined = date_joined
        if last_login is not None:
            self.last_login = last_login
        if is_active is not None:
            self.is_active = is_active
        if billcontact is not None:
            self.billcontact = billcontact

    @property
    def username(self):
        """Gets the username of this Body2.  # noqa: E501

        Required. 32 characters or fewer. Letters, digits and ./-/_ only.  # noqa: E501

        :return: The username of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Body2.

        Required. 32 characters or fewer. Letters, digits and ./-/_ only.  # noqa: E501

        :param username: The username of this Body2.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def type(self):
        """Gets the type of this Body2.  # noqa: E501


        :return: The type of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Body2.


        :param type: The type of this Body2.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def language(self):
        """Gets the language of this Body2.  # noqa: E501


        :return: The language of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Body2.


        :param language: The language of this Body2.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def short_name(self):
        """Gets the short_name of this Body2.  # noqa: E501


        :return: The short_name of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Body2.


        :param short_name: The short_name of this Body2.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def full_name(self):
        """Gets the full_name of this Body2.  # noqa: E501


        :return: The full_name of this Body2.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Body2.


        :param full_name: The full_name of this Body2.  # noqa: E501
        :type: str
        """
        if full_name is None:
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def date_joined(self):
        """Gets the date_joined of this Body2.  # noqa: E501


        :return: The date_joined of this Body2.  # noqa: E501
        :rtype: datetime
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """Sets the date_joined of this Body2.


        :param date_joined: The date_joined of this Body2.  # noqa: E501
        :type: datetime
        """

        self._date_joined = date_joined

    @property
    def last_login(self):
        """Gets the last_login of this Body2.  # noqa: E501


        :return: The last_login of this Body2.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this Body2.


        :param last_login: The last_login of this Body2.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def is_active(self):
        """Gets the is_active of this Body2.  # noqa: E501

        Designates whether this account should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :return: The is_active of this Body2.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Body2.

        Designates whether this account should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :param is_active: The is_active of this Body2.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def billcontact(self):
        """Gets the billcontact of this Body2.  # noqa: E501


        :return: The billcontact of this Body2.  # noqa: E501
        :rtype: ApiaccountsBillcontact
        """
        return self._billcontact

    @billcontact.setter
    def billcontact(self, billcontact):
        """Sets the billcontact of this Body2.


        :param billcontact: The billcontact of this Body2.  # noqa: E501
        :type: ApiaccountsBillcontact
        """

        self._billcontact = billcontact

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
        if issubclass(Body2, dict):
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
        if not isinstance(other, Body2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
