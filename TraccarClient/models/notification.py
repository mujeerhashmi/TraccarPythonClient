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


class Notification(object):
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
        'type': 'str',
        'always': 'bool',
        'web': 'bool',
        'mail': 'bool',
        'sms': 'bool',
        'calendar_id': 'int',
        'attributes': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'always': 'always',
        'web': 'web',
        'mail': 'mail',
        'sms': 'sms',
        'calendar_id': 'calendarId',
        'attributes': 'attributes'
    }

    def __init__(self, id=None, type=None, always=None, web=None, mail=None, sms=None, calendar_id=None, attributes=None):  # noqa: E501
        """Notification - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._always = None
        self._web = None
        self._mail = None
        self._sms = None
        self._calendar_id = None
        self._attributes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if always is not None:
            self.always = always
        if web is not None:
            self.web = web
        if mail is not None:
            self.mail = mail
        if sms is not None:
            self.sms = sms
        if calendar_id is not None:
            self.calendar_id = calendar_id
        if attributes is not None:
            self.attributes = attributes

    @property
    def id(self):
        """Gets the id of this Notification.  # noqa: E501


        :return: The id of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Notification.


        :param id: The id of this Notification.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Notification.  # noqa: E501


        :return: The type of this Notification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Notification.


        :param type: The type of this Notification.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def always(self):
        """Gets the always of this Notification.  # noqa: E501


        :return: The always of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._always

    @always.setter
    def always(self, always):
        """Sets the always of this Notification.


        :param always: The always of this Notification.  # noqa: E501
        :type: bool
        """

        self._always = always

    @property
    def web(self):
        """Gets the web of this Notification.  # noqa: E501


        :return: The web of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._web

    @web.setter
    def web(self, web):
        """Sets the web of this Notification.


        :param web: The web of this Notification.  # noqa: E501
        :type: bool
        """

        self._web = web

    @property
    def mail(self):
        """Gets the mail of this Notification.  # noqa: E501


        :return: The mail of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._mail

    @mail.setter
    def mail(self, mail):
        """Sets the mail of this Notification.


        :param mail: The mail of this Notification.  # noqa: E501
        :type: bool
        """

        self._mail = mail

    @property
    def sms(self):
        """Gets the sms of this Notification.  # noqa: E501


        :return: The sms of this Notification.  # noqa: E501
        :rtype: bool
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this Notification.


        :param sms: The sms of this Notification.  # noqa: E501
        :type: bool
        """

        self._sms = sms

    @property
    def calendar_id(self):
        """Gets the calendar_id of this Notification.  # noqa: E501


        :return: The calendar_id of this Notification.  # noqa: E501
        :rtype: int
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this Notification.


        :param calendar_id: The calendar_id of this Notification.  # noqa: E501
        :type: int
        """

        self._calendar_id = calendar_id

    @property
    def attributes(self):
        """Gets the attributes of this Notification.  # noqa: E501


        :return: The attributes of this Notification.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Notification.


        :param attributes: The attributes of this Notification.  # noqa: E501
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
        if issubclass(Notification, dict):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
