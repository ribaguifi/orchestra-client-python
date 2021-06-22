# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse2005(object):
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
        'number': 'str',
        'type': 'str',
        'total': 'str',
        'is_sent': 'bool',
        'created_on': 'date',
        'due_on': 'date',
        'comments': 'str'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'number': 'number',
        'type': 'type',
        'total': 'total',
        'is_sent': 'is_sent',
        'created_on': 'created_on',
        'due_on': 'due_on',
        'comments': 'comments'
    }

    def __init__(self, url=None, id=None, number=None, type=None, total=None, is_sent=None, created_on=None, due_on=None, comments=None):  # noqa: E501
        """InlineResponse2005 - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._id = None
        self._number = None
        self._type = None
        self._total = None
        self._is_sent = None
        self._created_on = None
        self._due_on = None
        self._comments = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        self.type = type
        if total is not None:
            self.total = total
        if is_sent is not None:
            self.is_sent = is_sent
        if created_on is not None:
            self.created_on = created_on
        if due_on is not None:
            self.due_on = due_on
        if comments is not None:
            self.comments = comments

    @property
    def url(self):
        """Gets the url of this InlineResponse2005.  # noqa: E501


        :return: The url of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse2005.


        :param url: The url of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this InlineResponse2005.  # noqa: E501


        :return: The id of this InlineResponse2005.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse2005.


        :param id: The id of this InlineResponse2005.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def number(self):
        """Gets the number of this InlineResponse2005.  # noqa: E501


        :return: The number of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this InlineResponse2005.


        :param number: The number of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def type(self):
        """Gets the type of this InlineResponse2005.  # noqa: E501


        :return: The type of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse2005.


        :param type: The type of this InlineResponse2005.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def total(self):
        """Gets the total of this InlineResponse2005.  # noqa: E501


        :return: The total of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse2005.


        :param total: The total of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def is_sent(self):
        """Gets the is_sent of this InlineResponse2005.  # noqa: E501


        :return: The is_sent of this InlineResponse2005.  # noqa: E501
        :rtype: bool
        """
        return self._is_sent

    @is_sent.setter
    def is_sent(self, is_sent):
        """Sets the is_sent of this InlineResponse2005.


        :param is_sent: The is_sent of this InlineResponse2005.  # noqa: E501
        :type: bool
        """

        self._is_sent = is_sent

    @property
    def created_on(self):
        """Gets the created_on of this InlineResponse2005.  # noqa: E501


        :return: The created_on of this InlineResponse2005.  # noqa: E501
        :rtype: date
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InlineResponse2005.


        :param created_on: The created_on of this InlineResponse2005.  # noqa: E501
        :type: date
        """

        self._created_on = created_on

    @property
    def due_on(self):
        """Gets the due_on of this InlineResponse2005.  # noqa: E501


        :return: The due_on of this InlineResponse2005.  # noqa: E501
        :rtype: date
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this InlineResponse2005.


        :param due_on: The due_on of this InlineResponse2005.  # noqa: E501
        :type: date
        """

        self._due_on = due_on

    @property
    def comments(self):
        """Gets the comments of this InlineResponse2005.  # noqa: E501


        :return: The comments of this InlineResponse2005.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this InlineResponse2005.


        :param comments: The comments of this InlineResponse2005.  # noqa: E501
        :type: str
        """

        self._comments = comments

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
        if issubclass(InlineResponse2005, dict):
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
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other