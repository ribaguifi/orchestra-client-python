# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Body95(object):
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
        'domain': 'ApimailboxesDomain',
        'mailboxes': 'list[ApiaddressesMailboxes]',
        'forward': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain': 'domain',
        'mailboxes': 'mailboxes',
        'forward': 'forward'
    }

    def __init__(self, name=None, domain=None, mailboxes=None, forward=None):  # noqa: E501
        """Body95 - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._domain = None
        self._mailboxes = None
        self._forward = None
        self.discriminator = None
        self.name = name
        self.domain = domain
        if mailboxes is not None:
            self.mailboxes = mailboxes
        if forward is not None:
            self.forward = forward

    @property
    def name(self):
        """Gets the name of this Body95.  # noqa: E501

        Address name, left blank for a <i>catch-all</i> address  # noqa: E501

        :return: The name of this Body95.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Body95.

        Address name, left blank for a <i>catch-all</i> address  # noqa: E501

        :param name: The name of this Body95.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain(self):
        """Gets the domain of this Body95.  # noqa: E501


        :return: The domain of this Body95.  # noqa: E501
        :rtype: ApimailboxesDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Body95.


        :param domain: The domain of this Body95.  # noqa: E501
        :type: ApimailboxesDomain
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def mailboxes(self):
        """Gets the mailboxes of this Body95.  # noqa: E501


        :return: The mailboxes of this Body95.  # noqa: E501
        :rtype: list[ApiaddressesMailboxes]
        """
        return self._mailboxes

    @mailboxes.setter
    def mailboxes(self, mailboxes):
        """Sets the mailboxes of this Body95.


        :param mailboxes: The mailboxes of this Body95.  # noqa: E501
        :type: list[ApiaddressesMailboxes]
        """

        self._mailboxes = mailboxes

    @property
    def forward(self):
        """Gets the forward of this Body95.  # noqa: E501

        Space separated email addresses or mailboxes  # noqa: E501

        :return: The forward of this Body95.  # noqa: E501
        :rtype: str
        """
        return self._forward

    @forward.setter
    def forward(self, forward):
        """Sets the forward of this Body95.

        Space separated email addresses or mailboxes  # noqa: E501

        :param forward: The forward of this Body95.  # noqa: E501
        :type: str
        """

        self._forward = forward

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
        if issubclass(Body95, dict):
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
        if not isinstance(other, Body95):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
