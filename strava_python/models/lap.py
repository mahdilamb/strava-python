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


class Lap(object):
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
        'activity': 'MetaActivity',
        'athlete': 'MetaAthlete',
        'average_cadence': 'float',
        'average_speed': 'float',
        'distance': 'float',
        'elapsed_time': 'int',
        'start_index': 'int',
        'end_index': 'int',
        'lap_index': 'int',
        'max_speed': 'float',
        'moving_time': 'int',
        'name': 'str',
        'pace_zone': 'int',
        'split': 'int',
        'start_date': 'datetime',
        'start_date_local': 'datetime',
        'total_elevation_gain': 'float'
    }

    attribute_map = {
        'id': 'id',
        'activity': 'activity',
        'athlete': 'athlete',
        'average_cadence': 'average_cadence',
        'average_speed': 'average_speed',
        'distance': 'distance',
        'elapsed_time': 'elapsed_time',
        'start_index': 'start_index',
        'end_index': 'end_index',
        'lap_index': 'lap_index',
        'max_speed': 'max_speed',
        'moving_time': 'moving_time',
        'name': 'name',
        'pace_zone': 'pace_zone',
        'split': 'split',
        'start_date': 'start_date',
        'start_date_local': 'start_date_local',
        'total_elevation_gain': 'total_elevation_gain'
    }

    def __init__(self, id=None, activity=None, athlete=None, average_cadence=None, average_speed=None, distance=None, elapsed_time=None, start_index=None, end_index=None, lap_index=None, max_speed=None, moving_time=None, name=None, pace_zone=None, split=None, start_date=None, start_date_local=None, total_elevation_gain=None, _configuration=None):  # noqa: E501
        """Lap - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._activity = None
        self._athlete = None
        self._average_cadence = None
        self._average_speed = None
        self._distance = None
        self._elapsed_time = None
        self._start_index = None
        self._end_index = None
        self._lap_index = None
        self._max_speed = None
        self._moving_time = None
        self._name = None
        self._pace_zone = None
        self._split = None
        self._start_date = None
        self._start_date_local = None
        self._total_elevation_gain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if activity is not None:
            self.activity = activity
        if athlete is not None:
            self.athlete = athlete
        if average_cadence is not None:
            self.average_cadence = average_cadence
        if average_speed is not None:
            self.average_speed = average_speed
        if distance is not None:
            self.distance = distance
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if start_index is not None:
            self.start_index = start_index
        if end_index is not None:
            self.end_index = end_index
        if lap_index is not None:
            self.lap_index = lap_index
        if max_speed is not None:
            self.max_speed = max_speed
        if moving_time is not None:
            self.moving_time = moving_time
        if name is not None:
            self.name = name
        if pace_zone is not None:
            self.pace_zone = pace_zone
        if split is not None:
            self.split = split
        if start_date is not None:
            self.start_date = start_date
        if start_date_local is not None:
            self.start_date_local = start_date_local
        if total_elevation_gain is not None:
            self.total_elevation_gain = total_elevation_gain

    @property
    def id(self):
        """Gets the id of this Lap.  # noqa: E501

        The unique identifier of this lap  # noqa: E501

        :return: The id of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Lap.

        The unique identifier of this lap  # noqa: E501

        :param id: The id of this Lap.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def activity(self):
        """Gets the activity of this Lap.  # noqa: E501


        :return: The activity of this Lap.  # noqa: E501
        :rtype: MetaActivity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this Lap.


        :param activity: The activity of this Lap.  # noqa: E501
        :type: MetaActivity
        """

        self._activity = activity

    @property
    def athlete(self):
        """Gets the athlete of this Lap.  # noqa: E501


        :return: The athlete of this Lap.  # noqa: E501
        :rtype: MetaAthlete
        """
        return self._athlete

    @athlete.setter
    def athlete(self, athlete):
        """Sets the athlete of this Lap.


        :param athlete: The athlete of this Lap.  # noqa: E501
        :type: MetaAthlete
        """

        self._athlete = athlete

    @property
    def average_cadence(self):
        """Gets the average_cadence of this Lap.  # noqa: E501

        The lap's average cadence  # noqa: E501

        :return: The average_cadence of this Lap.  # noqa: E501
        :rtype: float
        """
        return self._average_cadence

    @average_cadence.setter
    def average_cadence(self, average_cadence):
        """Sets the average_cadence of this Lap.

        The lap's average cadence  # noqa: E501

        :param average_cadence: The average_cadence of this Lap.  # noqa: E501
        :type: float
        """

        self._average_cadence = average_cadence

    @property
    def average_speed(self):
        """Gets the average_speed of this Lap.  # noqa: E501

        The lap's average speed  # noqa: E501

        :return: The average_speed of this Lap.  # noqa: E501
        :rtype: float
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, average_speed):
        """Sets the average_speed of this Lap.

        The lap's average speed  # noqa: E501

        :param average_speed: The average_speed of this Lap.  # noqa: E501
        :type: float
        """

        self._average_speed = average_speed

    @property
    def distance(self):
        """Gets the distance of this Lap.  # noqa: E501

        The lap's distance, in meters  # noqa: E501

        :return: The distance of this Lap.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Lap.

        The lap's distance, in meters  # noqa: E501

        :param distance: The distance of this Lap.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this Lap.  # noqa: E501

        The lap's elapsed time, in seconds  # noqa: E501

        :return: The elapsed_time of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this Lap.

        The lap's elapsed time, in seconds  # noqa: E501

        :param elapsed_time: The elapsed_time of this Lap.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def start_index(self):
        """Gets the start_index of this Lap.  # noqa: E501

        The start index of this effort in its activity's stream  # noqa: E501

        :return: The start_index of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._start_index

    @start_index.setter
    def start_index(self, start_index):
        """Sets the start_index of this Lap.

        The start index of this effort in its activity's stream  # noqa: E501

        :param start_index: The start_index of this Lap.  # noqa: E501
        :type: int
        """

        self._start_index = start_index

    @property
    def end_index(self):
        """Gets the end_index of this Lap.  # noqa: E501

        The end index of this effort in its activity's stream  # noqa: E501

        :return: The end_index of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._end_index

    @end_index.setter
    def end_index(self, end_index):
        """Sets the end_index of this Lap.

        The end index of this effort in its activity's stream  # noqa: E501

        :param end_index: The end_index of this Lap.  # noqa: E501
        :type: int
        """

        self._end_index = end_index

    @property
    def lap_index(self):
        """Gets the lap_index of this Lap.  # noqa: E501

        The index of this lap in the activity it belongs to  # noqa: E501

        :return: The lap_index of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._lap_index

    @lap_index.setter
    def lap_index(self, lap_index):
        """Sets the lap_index of this Lap.

        The index of this lap in the activity it belongs to  # noqa: E501

        :param lap_index: The lap_index of this Lap.  # noqa: E501
        :type: int
        """

        self._lap_index = lap_index

    @property
    def max_speed(self):
        """Gets the max_speed of this Lap.  # noqa: E501

        The maximum speed of this lat, in meters per second  # noqa: E501

        :return: The max_speed of this Lap.  # noqa: E501
        :rtype: float
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        """Sets the max_speed of this Lap.

        The maximum speed of this lat, in meters per second  # noqa: E501

        :param max_speed: The max_speed of this Lap.  # noqa: E501
        :type: float
        """

        self._max_speed = max_speed

    @property
    def moving_time(self):
        """Gets the moving_time of this Lap.  # noqa: E501

        The lap's moving time, in seconds  # noqa: E501

        :return: The moving_time of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._moving_time

    @moving_time.setter
    def moving_time(self, moving_time):
        """Sets the moving_time of this Lap.

        The lap's moving time, in seconds  # noqa: E501

        :param moving_time: The moving_time of this Lap.  # noqa: E501
        :type: int
        """

        self._moving_time = moving_time

    @property
    def name(self):
        """Gets the name of this Lap.  # noqa: E501

        The name of the lap  # noqa: E501

        :return: The name of this Lap.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Lap.

        The name of the lap  # noqa: E501

        :param name: The name of this Lap.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pace_zone(self):
        """Gets the pace_zone of this Lap.  # noqa: E501

        The athlete's pace zone during this lap  # noqa: E501

        :return: The pace_zone of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._pace_zone

    @pace_zone.setter
    def pace_zone(self, pace_zone):
        """Sets the pace_zone of this Lap.

        The athlete's pace zone during this lap  # noqa: E501

        :param pace_zone: The pace_zone of this Lap.  # noqa: E501
        :type: int
        """

        self._pace_zone = pace_zone

    @property
    def split(self):
        """Gets the split of this Lap.  # noqa: E501


        :return: The split of this Lap.  # noqa: E501
        :rtype: int
        """
        return self._split

    @split.setter
    def split(self, split):
        """Sets the split of this Lap.


        :param split: The split of this Lap.  # noqa: E501
        :type: int
        """

        self._split = split

    @property
    def start_date(self):
        """Gets the start_date of this Lap.  # noqa: E501

        The time at which the lap was started.  # noqa: E501

        :return: The start_date of this Lap.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Lap.

        The time at which the lap was started.  # noqa: E501

        :param start_date: The start_date of this Lap.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def start_date_local(self):
        """Gets the start_date_local of this Lap.  # noqa: E501

        The time at which the lap was started in the local timezone.  # noqa: E501

        :return: The start_date_local of this Lap.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_local

    @start_date_local.setter
    def start_date_local(self, start_date_local):
        """Sets the start_date_local of this Lap.

        The time at which the lap was started in the local timezone.  # noqa: E501

        :param start_date_local: The start_date_local of this Lap.  # noqa: E501
        :type: datetime
        """

        self._start_date_local = start_date_local

    @property
    def total_elevation_gain(self):
        """Gets the total_elevation_gain of this Lap.  # noqa: E501

        The elevation gain of this lap, in meters  # noqa: E501

        :return: The total_elevation_gain of this Lap.  # noqa: E501
        :rtype: float
        """
        return self._total_elevation_gain

    @total_elevation_gain.setter
    def total_elevation_gain(self, total_elevation_gain):
        """Sets the total_elevation_gain of this Lap.

        The elevation gain of this lap, in meters  # noqa: E501

        :param total_elevation_gain: The total_elevation_gain of this Lap.  # noqa: E501
        :type: float
        """

        self._total_elevation_gain = total_elevation_gain

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
        if issubclass(Lap, dict):
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
        if not isinstance(other, Lap):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Lap):
            return True

        return self.to_dict() != other.to_dict()
