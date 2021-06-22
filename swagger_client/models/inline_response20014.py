# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20014(object):
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
        'filtering': 'str',
        'custom_filtering': 'str',
        'addresses': 'list[ApimailboxesAddresses]',
        'is_active': 'bool',
        'resources': 'list[ApimailboxesResources]'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'name': 'name',
        'filtering': 'filtering',
        'custom_filtering': 'custom_filtering',
        'addresses': 'addresses',
        'is_active': 'is_active',
        'resources': 'resources'
    }

    def __init__(self, url=None, id=None, name=None, filtering=None, custom_filtering=None, addresses=None, is_active=None, resources=None):  # noqa: E501
        """InlineResponse20014 - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._id = None
        self._name = None
        self._filtering = None
        self._custom_filtering = None
        self._addresses = None
        self._is_active = None
        self._resources = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        self.name = name
        if filtering is not None:
            self.filtering = filtering
        if custom_filtering is not None:
            self.custom_filtering = custom_filtering
        if addresses is not None:
            self.addresses = addresses
        if is_active is not None:
            self.is_active = is_active
        if resources is not None:
            self.resources = resources

    @property
    def url(self):
        """Gets the url of this InlineResponse20014.  # noqa: E501


        :return: The url of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20014.


        :param url: The url of this InlineResponse20014.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this InlineResponse20014.  # noqa: E501


        :return: The id of this InlineResponse20014.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20014.


        :param id: The id of this InlineResponse20014.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20014.  # noqa: E501

        Required. 32 characters or fewer. Letters, digits and ./-/_ only.  # noqa: E501

        :return: The name of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20014.

        Required. 32 characters or fewer. Letters, digits and ./-/_ only.  # noqa: E501

        :param name: The name of this InlineResponse20014.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def filtering(self):
        """Gets the filtering of this InlineResponse20014.  # noqa: E501


        :return: The filtering of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._filtering

    @filtering.setter
    def filtering(self, filtering):
        """Sets the filtering of this InlineResponse20014.


        :param filtering: The filtering of this InlineResponse20014.  # noqa: E501
        :type: str
        """

        self._filtering = filtering

    @property
    def custom_filtering(self):
        """Gets the custom_filtering of this InlineResponse20014.  # noqa: E501

        Arbitrary email filtering in <a href='https://tty1.net/blog/2011/sieve-tutorial_en.html'>sieve language</a>. This overrides any automatic junk email filtering  # noqa: E501

        :return: The custom_filtering of this InlineResponse20014.  # noqa: E501
        :rtype: str
        """
        return self._custom_filtering

    @custom_filtering.setter
    def custom_filtering(self, custom_filtering):
        """Sets the custom_filtering of this InlineResponse20014.

        Arbitrary email filtering in <a href='https://tty1.net/blog/2011/sieve-tutorial_en.html'>sieve language</a>. This overrides any automatic junk email filtering  # noqa: E501

        :param custom_filtering: The custom_filtering of this InlineResponse20014.  # noqa: E501
        :type: str
        """

        self._custom_filtering = custom_filtering

    @property
    def addresses(self):
        """Gets the addresses of this InlineResponse20014.  # noqa: E501


        :return: The addresses of this InlineResponse20014.  # noqa: E501
        :rtype: list[ApimailboxesAddresses]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this InlineResponse20014.


        :param addresses: The addresses of this InlineResponse20014.  # noqa: E501
        :type: list[ApimailboxesAddresses]
        """

        self._addresses = addresses

    @property
    def is_active(self):
        """Gets the is_active of this InlineResponse20014.  # noqa: E501


        :return: The is_active of this InlineResponse20014.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this InlineResponse20014.


        :param is_active: The is_active of this InlineResponse20014.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def resources(self):
        """Gets the resources of this InlineResponse20014.  # noqa: E501


        :return: The resources of this InlineResponse20014.  # noqa: E501
        :rtype: list[ApimailboxesResources]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this InlineResponse20014.


        :param resources: The resources of this InlineResponse20014.  # noqa: E501
        :type: list[ApimailboxesResources]
        """

        self._resources = resources

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
        if issubclass(InlineResponse20014, dict):
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
        if not isinstance(other, InlineResponse20014):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
