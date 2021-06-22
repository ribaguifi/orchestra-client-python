# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ApiticketsMessages(object):
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
        'id': 'int',
        'author': 'str',
        'author_name': 'str',
        'content': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'author': 'author',
        'author_name': 'author_name',
        'content': 'content',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, author=None, author_name=None, content=None, created_at=None):  # noqa: E501
        """ApiticketsMessages - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._author = None
        self._author_name = None
        self._content = None
        self._created_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if author is not None:
            self.author = author
        if author_name is not None:
            self.author_name = author_name
        self.content = content
        if created_at is not None:
            self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this ApiticketsMessages.  # noqa: E501


        :return: The id of this ApiticketsMessages.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiticketsMessages.


        :param id: The id of this ApiticketsMessages.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def author(self):
        """Gets the author of this ApiticketsMessages.  # noqa: E501


        :return: The author of this ApiticketsMessages.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ApiticketsMessages.


        :param author: The author of this ApiticketsMessages.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def author_name(self):
        """Gets the author_name of this ApiticketsMessages.  # noqa: E501


        :return: The author_name of this ApiticketsMessages.  # noqa: E501
        :rtype: str
        """
        return self._author_name

    @author_name.setter
    def author_name(self, author_name):
        """Sets the author_name of this ApiticketsMessages.


        :param author_name: The author_name of this ApiticketsMessages.  # noqa: E501
        :type: str
        """

        self._author_name = author_name

    @property
    def content(self):
        """Gets the content of this ApiticketsMessages.  # noqa: E501


        :return: The content of this ApiticketsMessages.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ApiticketsMessages.


        :param content: The content of this ApiticketsMessages.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def created_at(self):
        """Gets the created_at of this ApiticketsMessages.  # noqa: E501


        :return: The created_at of this ApiticketsMessages.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiticketsMessages.


        :param created_at: The created_at of this ApiticketsMessages.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if issubclass(ApiticketsMessages, dict):
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
        if not isinstance(other, ApiticketsMessages):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
