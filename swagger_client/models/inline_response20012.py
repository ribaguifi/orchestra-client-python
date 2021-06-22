# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20012(object):
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
        'records': 'list[ApidomainsRecords]'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'name': 'name',
        'records': 'records'
    }

    def __init__(self, url=None, id=None, name=None, records=None):  # noqa: E501
        """InlineResponse20012 - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._id = None
        self._name = None
        self._records = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        self.name = name
        if records is not None:
            self.records = records

    @property
    def url(self):
        """Gets the url of this InlineResponse20012.  # noqa: E501


        :return: The url of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse20012.


        :param url: The url of this InlineResponse20012.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this InlineResponse20012.  # noqa: E501


        :return: The id of this InlineResponse20012.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20012.


        :param id: The id of this InlineResponse20012.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20012.  # noqa: E501

        Domain or subdomain name.  # noqa: E501

        :return: The name of this InlineResponse20012.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20012.

        Domain or subdomain name.  # noqa: E501

        :param name: The name of this InlineResponse20012.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def records(self):
        """Gets the records of this InlineResponse20012.  # noqa: E501


        :return: The records of this InlineResponse20012.  # noqa: E501
        :rtype: list[ApidomainsRecords]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this InlineResponse20012.


        :param records: The records of this InlineResponse20012.  # noqa: E501
        :type: list[ApidomainsRecords]
        """

        self._records = records

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
        if issubclass(InlineResponse20012, dict):
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
        if not isinstance(other, InlineResponse20012):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
