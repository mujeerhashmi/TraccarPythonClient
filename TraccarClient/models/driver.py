# coding: utf-8

"""
    4CS GPS Tracking System

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Driver(object):
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
        'name': 'str',
        'unique_id': 'str',
        'attributes': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'unique_id': 'uniqueId',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, name=None, unique_id=None, attributes=None):  # noqa: E501
        """Driver - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._unique_id = None
        self._attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if unique_id is not None:
            self.unique_id = unique_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this Driver.  # noqa: E501


        :return: The id of this Driver.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Driver.


        :param id: The id of this Driver.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Driver.  # noqa: E501


        :return: The name of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Driver.


        :param name: The name of this Driver.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def unique_id(self):
        """Gets the unique_id of this Driver.  # noqa: E501


        :return: The unique_id of this Driver.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this Driver.


        :param unique_id: The unique_id of this Driver.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def attributes(self):
        """Gets the attributes of this Driver.  # noqa: E501


        :return: The attributes of this Driver.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Driver.


        :param attributes: The attributes of this Driver.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

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
        if issubclass(Driver, dict):
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
        if not isinstance(other, Driver):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
