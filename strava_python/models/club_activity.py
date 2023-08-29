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


class ClubActivity(object):
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
        'athlete': 'MetaAthlete',
        'name': 'str',
        'distance': 'float',
        'moving_time': 'int',
        'elapsed_time': 'int',
        'total_elevation_gain': 'float',
        'type': 'ActivityType',
        'sport_type': 'SportType',
        'workout_type': 'int'
    }

    attribute_map = {
        'athlete': 'athlete',
        'name': 'name',
        'distance': 'distance',
        'moving_time': 'moving_time',
        'elapsed_time': 'elapsed_time',
        'total_elevation_gain': 'total_elevation_gain',
        'type': 'type',
        'sport_type': 'sport_type',
        'workout_type': 'workout_type'
    }

    def __init__(self, athlete=None, name=None, distance=None, moving_time=None, elapsed_time=None, total_elevation_gain=None, type=None, sport_type=None, workout_type=None, _configuration=None):  # noqa: E501
        """ClubActivity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._athlete = None
        self._name = None
        self._distance = None
        self._moving_time = None
        self._elapsed_time = None
        self._total_elevation_gain = None
        self._type = None
        self._sport_type = None
        self._workout_type = None
        self.discriminator = None

        if athlete is not None:
            self.athlete = athlete
        if name is not None:
            self.name = name
        if distance is not None:
            self.distance = distance
        if moving_time is not None:
            self.moving_time = moving_time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if total_elevation_gain is not None:
            self.total_elevation_gain = total_elevation_gain
        if type is not None:
            self.type = type
        if sport_type is not None:
            self.sport_type = sport_type
        if workout_type is not None:
            self.workout_type = workout_type

    @property
    def athlete(self):
        """Gets the athlete of this ClubActivity.  # noqa: E501


        :return: The athlete of this ClubActivity.  # noqa: E501
        :rtype: MetaAthlete
        """
        return self._athlete

    @athlete.setter
    def athlete(self, athlete):
        """Sets the athlete of this ClubActivity.


        :param athlete: The athlete of this ClubActivity.  # noqa: E501
        :type: MetaAthlete
        """

        self._athlete = athlete

    @property
    def name(self):
        """Gets the name of this ClubActivity.  # noqa: E501

        The name of the activity  # noqa: E501

        :return: The name of this ClubActivity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClubActivity.

        The name of the activity  # noqa: E501

        :param name: The name of this ClubActivity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def distance(self):
        """Gets the distance of this ClubActivity.  # noqa: E501

        The activity's distance, in meters  # noqa: E501

        :return: The distance of this ClubActivity.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this ClubActivity.

        The activity's distance, in meters  # noqa: E501

        :param distance: The distance of this ClubActivity.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def moving_time(self):
        """Gets the moving_time of this ClubActivity.  # noqa: E501

        The activity's moving time, in seconds  # noqa: E501

        :return: The moving_time of this ClubActivity.  # noqa: E501
        :rtype: int
        """
        return self._moving_time

    @moving_time.setter
    def moving_time(self, moving_time):
        """Sets the moving_time of this ClubActivity.

        The activity's moving time, in seconds  # noqa: E501

        :param moving_time: The moving_time of this ClubActivity.  # noqa: E501
        :type: int
        """

        self._moving_time = moving_time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this ClubActivity.  # noqa: E501

        The activity's elapsed time, in seconds  # noqa: E501

        :return: The elapsed_time of this ClubActivity.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this ClubActivity.

        The activity's elapsed time, in seconds  # noqa: E501

        :param elapsed_time: The elapsed_time of this ClubActivity.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def total_elevation_gain(self):
        """Gets the total_elevation_gain of this ClubActivity.  # noqa: E501

        The activity's total elevation gain.  # noqa: E501

        :return: The total_elevation_gain of this ClubActivity.  # noqa: E501
        :rtype: float
        """
        return self._total_elevation_gain

    @total_elevation_gain.setter
    def total_elevation_gain(self, total_elevation_gain):
        """Sets the total_elevation_gain of this ClubActivity.

        The activity's total elevation gain.  # noqa: E501

        :param total_elevation_gain: The total_elevation_gain of this ClubActivity.  # noqa: E501
        :type: float
        """

        self._total_elevation_gain = total_elevation_gain

    @property
    def type(self):
        """Gets the type of this ClubActivity.  # noqa: E501

        Deprecated. Prefer to use sport_type  # noqa: E501

        :return: The type of this ClubActivity.  # noqa: E501
        :rtype: ActivityType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClubActivity.

        Deprecated. Prefer to use sport_type  # noqa: E501

        :param type: The type of this ClubActivity.  # noqa: E501
        :type: ActivityType
        """

        self._type = type

    @property
    def sport_type(self):
        """Gets the sport_type of this ClubActivity.  # noqa: E501


        :return: The sport_type of this ClubActivity.  # noqa: E501
        :rtype: SportType
        """
        return self._sport_type

    @sport_type.setter
    def sport_type(self, sport_type):
        """Sets the sport_type of this ClubActivity.


        :param sport_type: The sport_type of this ClubActivity.  # noqa: E501
        :type: SportType
        """

        self._sport_type = sport_type

    @property
    def workout_type(self):
        """Gets the workout_type of this ClubActivity.  # noqa: E501

        The activity's workout type  # noqa: E501

        :return: The workout_type of this ClubActivity.  # noqa: E501
        :rtype: int
        """
        return self._workout_type

    @workout_type.setter
    def workout_type(self, workout_type):
        """Sets the workout_type of this ClubActivity.

        The activity's workout type  # noqa: E501

        :param workout_type: The workout_type of this ClubActivity.  # noqa: E501
        :type: int
        """

        self._workout_type = workout_type

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
        if issubclass(ClubActivity, dict):
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
        if not isinstance(other, ClubActivity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClubActivity):
            return True

        return self.to_dict() != other.to_dict()
