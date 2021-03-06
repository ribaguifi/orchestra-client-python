# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20018(object):
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
        'url': 'str',
        'id': 'int',
        'name': 'str',
        'address_name': 'str',
        'address_domain': 'ApimailboxesDomain',
        'admin_email': 'str',
        'is_active': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'name': 'name',
        'address_name': 'address_name',
        'address_domain': 'address_domain',
        'admin_email': 'admin_email',
        'is_active': 'is_active'
    }

    def __init__(self, url=None, id=None, name=None, address_name=None, address_domain=None, admin_email=None, is_active=None):  # noqa: E501
        """InlineResponse20018 - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._id = None
        self._name = None
        self._address_name = None
        self._address_domain = None
        self._admin_email = None
        self._is_active = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        self.name = name
        self.address_name = address_name
        if address_domain is not None:
            self.address_domain = address_domain
        self.admin_email = admin_email
        if is_active is not None:
            self.is_active = is_active

    @property
    def url(self):
        """Gets the url of this InlineResponse20018.  # noqa: E501


        :return: The url of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20018.


        :param url: The url of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this InlineResponse20018.  # noqa: E501


        :return: The id of this InlineResponse20018.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20018.


        :param id: The id of this InlineResponse20018.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20018.  # noqa: E501

        Default list address &lt;name&gt;@lists.orchestra.lan  # noqa: E501

        :return: The name of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20018.

        Default list address &lt;name&gt;@lists.orchestra.lan  # noqa: E501

        :param name: The name of this InlineResponse20018.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address_name(self):
        """Gets the address_name of this InlineResponse20018.  # noqa: E501


        :return: The address_name of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._address_name

    @address_name.setter
    def address_name(self, address_name):
        """Sets the address_name of this InlineResponse20018.


        :param address_name: The address_name of this InlineResponse20018.  # noqa: E501
        :type: str
        """
        if address_name is None:
            raise ValueError("Invalid value for `address_name`, must not be `None`")  # noqa: E501

        self._address_name = address_name

    @property
    def address_domain(self):
        """Gets the address_domain of this InlineResponse20018.  # noqa: E501


        :return: The address_domain of this InlineResponse20018.  # noqa: E501
        :rtype: ApimailboxesDomain
        """
        return self._address_domain

    @address_domain.setter
    def address_domain(self, address_domain):
        """Sets the address_domain of this InlineResponse20018.


        :param address_domain: The address_domain of this InlineResponse20018.  # noqa: E501
        :type: ApimailboxesDomain
        """

        self._address_domain = address_domain

    @property
    def admin_email(self):
        """Gets the admin_email of this InlineResponse20018.  # noqa: E501

        Administration email address  # noqa: E501

        :return: The admin_email of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._admin_email

    @admin_email.setter
    def admin_email(self, admin_email):
        """Sets the admin_email of this InlineResponse20018.

        Administration email address  # noqa: E501

        :param admin_email: The admin_email of this InlineResponse20018.  # noqa: E501
        :type: str
        """
        if admin_email is None:
            raise ValueError("Invalid value for `admin_email`, must not be `None`")  # noqa: E501

        self._admin_email = admin_email

    @property
    def is_active(self):
        """Gets the is_active of this InlineResponse20018.  # noqa: E501

        Designates whether this account should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :return: The is_active of this InlineResponse20018.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this InlineResponse20018.

        Designates whether this account should be treated as active. Unselect this instead of deleting accounts.  # noqa: E501

        :param is_active: The is_active of this InlineResponse20018.  # noqa: E501
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
        if issubclass(InlineResponse20018, dict):
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
        if not isinstance(other, InlineResponse20018):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
