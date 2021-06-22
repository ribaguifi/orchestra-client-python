# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body12(object):
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
        'home': 'str',
        'directory': 'str',
        'shell': 'str',
        'groups': 'list[ApisystemusersGroups]',
        'is_active': 'bool'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'home': 'home',
        'directory': 'directory',
        'shell': 'shell',
        'groups': 'groups',
        'is_active': 'is_active'
    }

    def __init__(self, username=None, password=None, home=None, directory=None, shell=None, groups=None, is_active=None):  # noqa: E501
        """Body12 - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._home = None
        self._directory = None
        self._shell = None
        self._groups = None
        self._is_active = None
        self.discriminator = None
        self.username = username
        if password is not None:
            self.password = password
        if home is not None:
            self.home = home
        if directory is not None:
            self.directory = directory
        if shell is not None:
            self.shell = shell
        if groups is not None:
            self.groups = groups
        if is_active is not None:
            self.is_active = is_active

    @property
    def username(self):
        """Gets the username of this Body12.  # noqa: E501

        Required. 32 characters or fewer. Letters, digits and ./-/_ only.  # noqa: E501

        :return: The username of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Body12.

        Required. 32 characters or fewer. Letters, digits and ./-/_ only.  # noqa: E501

        :param username: The username of this Body12.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this Body12.  # noqa: E501


        :return: The password of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Body12.


        :param password: The password of this Body12.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def home(self):
        """Gets the home of this Body12.  # noqa: E501

        Starting location when login with this no-shell user.  # noqa: E501

        :return: The home of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._home

    @home.setter
    def home(self, home):
        """Sets the home of this Body12.

        Starting location when login with this no-shell user.  # noqa: E501

        :param home: The home of this Body12.  # noqa: E501
        :type: str
        """

        self._home = home

    @property
    def directory(self):
        """Gets the directory of this Body12.  # noqa: E501

        Optional directory relative to user's home.  # noqa: E501

        :return: The directory of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this Body12.

        Optional directory relative to user's home.  # noqa: E501

        :param directory: The directory of this Body12.  # noqa: E501
        :type: str
        """

        self._directory = directory

    @property
    def shell(self):
        """Gets the shell of this Body12.  # noqa: E501


        :return: The shell of this Body12.  # noqa: E501
        :rtype: str
        """
        return self._shell

    @shell.setter
    def shell(self, shell):
        """Sets the shell of this Body12.


        :param shell: The shell of this Body12.  # noqa: E501
        :type: str
        """

        self._shell = shell

    @property
    def groups(self):
        """Gets the groups of this Body12.  # noqa: E501


        :return: The groups of this Body12.  # noqa: E501
        :rtype: list[ApisystemusersGroups]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Body12.


        :param groups: The groups of this Body12.  # noqa: E501
        :type: list[ApisystemusersGroups]
        """

        self._groups = groups

    @property
    def is_active(self):
        """Gets the is_active of this Body12.  # noqa: E501

        Designates whether this account should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :return: The is_active of this Body12.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Body12.

        Designates whether this account should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :param is_active: The is_active of this Body12.  # noqa: E501
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
        if issubclass(Body12, dict):
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
        if not isinstance(other, Body12):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
