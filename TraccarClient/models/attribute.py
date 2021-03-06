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


class Attribute(object):
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
        'description': 'str',
        'attribute': 'str',
        'expression': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'attribute': 'attribute',
        'expression': 'expression',
        'type': 'type'
    }

    def __init__(self, id=None, description=None, attribute=None, expression=None, type=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._description = None
        self._attribute = None
        self._expression = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if attribute is not None:
            self.attribute = attribute
        if expression is not None:
            self.expression = expression
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this Attribute.  # noqa: E501


        :return: The id of this Attribute.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Attribute.


        :param id: The id of this Attribute.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this Attribute.  # noqa: E501


        :return: The description of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Attribute.


        :param description: The description of this Attribute.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def attribute(self):
        """Gets the attribute of this Attribute.  # noqa: E501


        :return: The attribute of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this Attribute.


        :param attribute: The attribute of this Attribute.  # noqa: E501
        :type: str
        """

        self._attribute = attribute

    @property
    def expression(self):
        """Gets the expression of this Attribute.  # noqa: E501


        :return: The expression of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this Attribute.


        :param expression: The expression of this Attribute.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def type(self):
        """Gets the type of this Attribute.  # noqa: E501

        String|Number|Boolean  # noqa: E501

        :return: The type of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Attribute.

        String|Number|Boolean  # noqa: E501

        :param type: The type of this Attribute.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
