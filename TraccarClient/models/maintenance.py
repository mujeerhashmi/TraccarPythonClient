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


class Maintenance(object):
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
        'type': 'str',
        'start': 'float',
        'period': 'float',
        'attributes': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'start': 'start',
        'period': 'period',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, name=None, type=None, start=None, period=None, attributes=None):  # noqa: E501
        """Maintenance - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._type = None
        self._start = None
        self._period = None
        self._attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if start is not None:
            self.start = start
        if period is not None:
            self.period = period
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this Maintenance.  # noqa: E501


        :return: The id of this Maintenance.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Maintenance.


        :param id: The id of this Maintenance.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Maintenance.  # noqa: E501


        :return: The name of this Maintenance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Maintenance.


        :param name: The name of this Maintenance.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Maintenance.  # noqa: E501


        :return: The type of this Maintenance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Maintenance.


        :param type: The type of this Maintenance.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def start(self):
        """Gets the start of this Maintenance.  # noqa: E501


        :return: The start of this Maintenance.  # noqa: E501
        :rtype: float
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this Maintenance.


        :param start: The start of this Maintenance.  # noqa: E501
        :type: float
        """

        self._start = start

    @property
    def period(self):
        """Gets the period of this Maintenance.  # noqa: E501


        :return: The period of this Maintenance.  # noqa: E501
        :rtype: float
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Maintenance.


        :param period: The period of this Maintenance.  # noqa: E501
        :type: float
        """

        self._period = period

    @property
    def attributes(self):
        """Gets the attributes of this Maintenance.  # noqa: E501


        :return: The attributes of this Maintenance.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Maintenance.


        :param attributes: The attributes of this Maintenance.  # noqa: E501
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
        if issubclass(Maintenance, dict):
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
        if not isinstance(other, Maintenance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
