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


class Statistics(object):
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
        'capture_time': 'datetime',
        'active_users': 'int',
        'active_devices': 'int',
        'requests': 'int',
        'messages_received': 'int',
        'messages_stored': 'int'
    }

    attribute_map = {
        'capture_time': 'captureTime',
        'active_users': 'activeUsers',
        'active_devices': 'activeDevices',
        'requests': 'requests',
        'messages_received': 'messagesReceived',
        'messages_stored': 'messagesStored'
    }

    def __init__(self, capture_time=None, active_users=None, active_devices=None, requests=None, messages_received=None, messages_stored=None):  # noqa: E501
        """Statistics - a model defined in Swagger"""  # noqa: E501

        self._capture_time = None
        self._active_users = None
        self._active_devices = None
        self._requests = None
        self._messages_received = None
        self._messages_stored = None
        self.discriminator = None

        if capture_time is not None:
            self.capture_time = capture_time
        if active_users is not None:
            self.active_users = active_users
        if active_devices is not None:
            self.active_devices = active_devices
        if requests is not None:
            self.requests = requests
        if messages_received is not None:
            self.messages_received = messages_received
        if messages_stored is not None:
            self.messages_stored = messages_stored

    @property
    def capture_time(self):
        """Gets the capture_time of this Statistics.  # noqa: E501

        in IS0 8601 format. eg. `1963-11-22T18:30:00Z`  # noqa: E501

        :return: The capture_time of this Statistics.  # noqa: E501
        :rtype: datetime
        """
        return self._capture_time

    @capture_time.setter
    def capture_time(self, capture_time):
        """Sets the capture_time of this Statistics.

        in IS0 8601 format. eg. `1963-11-22T18:30:00Z`  # noqa: E501

        :param capture_time: The capture_time of this Statistics.  # noqa: E501
        :type: datetime
        """

        self._capture_time = capture_time

    @property
    def active_users(self):
        """Gets the active_users of this Statistics.  # noqa: E501


        :return: The active_users of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._active_users

    @active_users.setter
    def active_users(self, active_users):
        """Sets the active_users of this Statistics.


        :param active_users: The active_users of this Statistics.  # noqa: E501
        :type: int
        """

        self._active_users = active_users

    @property
    def active_devices(self):
        """Gets the active_devices of this Statistics.  # noqa: E501


        :return: The active_devices of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._active_devices

    @active_devices.setter
    def active_devices(self, active_devices):
        """Sets the active_devices of this Statistics.


        :param active_devices: The active_devices of this Statistics.  # noqa: E501
        :type: int
        """

        self._active_devices = active_devices

    @property
    def requests(self):
        """Gets the requests of this Statistics.  # noqa: E501


        :return: The requests of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this Statistics.


        :param requests: The requests of this Statistics.  # noqa: E501
        :type: int
        """

        self._requests = requests

    @property
    def messages_received(self):
        """Gets the messages_received of this Statistics.  # noqa: E501


        :return: The messages_received of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._messages_received

    @messages_received.setter
    def messages_received(self, messages_received):
        """Sets the messages_received of this Statistics.


        :param messages_received: The messages_received of this Statistics.  # noqa: E501
        :type: int
        """

        self._messages_received = messages_received

    @property
    def messages_stored(self):
        """Gets the messages_stored of this Statistics.  # noqa: E501


        :return: The messages_stored of this Statistics.  # noqa: E501
        :rtype: int
        """
        return self._messages_stored

    @messages_stored.setter
    def messages_stored(self, messages_stored):
        """Sets the messages_stored of this Statistics.


        :param messages_stored: The messages_stored of this Statistics.  # noqa: E501
        :type: int
        """

        self._messages_stored = messages_stored

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
        if issubclass(Statistics, dict):
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
        if not isinstance(other, Statistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
