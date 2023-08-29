# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from strava_python.configuration import Configuration


class PhotosSummary(object):
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
        'count': 'int',
        'primary': 'PhotosSummaryPrimary'
    }

    attribute_map = {
        'count': 'count',
        'primary': 'primary'
    }

    def __init__(self, count=None, primary=None, _configuration=None):  # noqa: E501
        """PhotosSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._primary = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if primary is not None:
            self.primary = primary

    @property
    def count(self):
        """Gets the count of this PhotosSummary.  # noqa: E501

        The number of photos  # noqa: E501

        :return: The count of this PhotosSummary.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PhotosSummary.

        The number of photos  # noqa: E501

        :param count: The count of this PhotosSummary.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def primary(self):
        """Gets the primary of this PhotosSummary.  # noqa: E501


        :return: The primary of this PhotosSummary.  # noqa: E501
        :rtype: PhotosSummaryPrimary
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this PhotosSummary.


        :param primary: The primary of this PhotosSummary.  # noqa: E501
        :type: PhotosSummaryPrimary
        """

        self._primary = primary

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
        if issubclass(PhotosSummary, dict):
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
        if not isinstance(other, PhotosSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhotosSummary):
            return True

        return self.to_dict() != other.to_dict()
