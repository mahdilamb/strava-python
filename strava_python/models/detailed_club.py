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


class DetailedClub(object):
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
        'membership': 'str',
        'admin': 'bool',
        'owner': 'bool',
        'following_count': 'int'
    }

    attribute_map = {
        'membership': 'membership',
        'admin': 'admin',
        'owner': 'owner',
        'following_count': 'following_count'
    }

    def __init__(self, membership=None, admin=None, owner=None, following_count=None, _configuration=None):  # noqa: E501
        """DetailedClub - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._membership = None
        self._admin = None
        self._owner = None
        self._following_count = None
        self.discriminator = None

        if membership is not None:
            self.membership = membership
        if admin is not None:
            self.admin = admin
        if owner is not None:
            self.owner = owner
        if following_count is not None:
            self.following_count = following_count

    @property
    def membership(self):
        """Gets the membership of this DetailedClub.  # noqa: E501

        The membership status of the logged-in athlete.  # noqa: E501

        :return: The membership of this DetailedClub.  # noqa: E501
        :rtype: str
        """
        return self._membership

    @membership.setter
    def membership(self, membership):
        """Sets the membership of this DetailedClub.

        The membership status of the logged-in athlete.  # noqa: E501

        :param membership: The membership of this DetailedClub.  # noqa: E501
        :type: str
        """
        allowed_values = ["member", "pending"]  # noqa: E501
        if (self._configuration.client_side_validation and
                membership not in allowed_values):
            raise ValueError(
                "Invalid value for `membership` ({0}), must be one of {1}"  # noqa: E501
                .format(membership, allowed_values)
            )

        self._membership = membership

    @property
    def admin(self):
        """Gets the admin of this DetailedClub.  # noqa: E501

        Whether the currently logged-in athlete is an administrator of this club.  # noqa: E501

        :return: The admin of this DetailedClub.  # noqa: E501
        :rtype: bool
        """
        return self._admin

    @admin.setter
    def admin(self, admin):
        """Sets the admin of this DetailedClub.

        Whether the currently logged-in athlete is an administrator of this club.  # noqa: E501

        :param admin: The admin of this DetailedClub.  # noqa: E501
        :type: bool
        """

        self._admin = admin

    @property
    def owner(self):
        """Gets the owner of this DetailedClub.  # noqa: E501

        Whether the currently logged-in athlete is the owner of this club.  # noqa: E501

        :return: The owner of this DetailedClub.  # noqa: E501
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DetailedClub.

        Whether the currently logged-in athlete is the owner of this club.  # noqa: E501

        :param owner: The owner of this DetailedClub.  # noqa: E501
        :type: bool
        """

        self._owner = owner

    @property
    def following_count(self):
        """Gets the following_count of this DetailedClub.  # noqa: E501

        The number of athletes in the club that the logged-in athlete follows.  # noqa: E501

        :return: The following_count of this DetailedClub.  # noqa: E501
        :rtype: int
        """
        return self._following_count

    @following_count.setter
    def following_count(self, following_count):
        """Sets the following_count of this DetailedClub.

        The number of athletes in the club that the logged-in athlete follows.  # noqa: E501

        :param following_count: The following_count of this DetailedClub.  # noqa: E501
        :type: int
        """

        self._following_count = following_count

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
        if issubclass(DetailedClub, dict):
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
        if not isinstance(other, DetailedClub):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailedClub):
            return True

        return self.to_dict() != other.to_dict()
