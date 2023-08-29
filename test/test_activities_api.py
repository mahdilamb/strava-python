# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import strava_python
from strava_python.api.activities_api import ActivitiesApi  # noqa: E501
from strava_python.rest import ApiException


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.api = strava_python.api.activities_api.ActivitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_activity(self):
        """Test case for create_activity

        Create an Activity  # noqa: E501
        """
        pass

    def test_get_activity_by_id(self):
        """Test case for get_activity_by_id

        Get Activity  # noqa: E501
        """
        pass

    def test_get_comments_by_activity_id(self):
        """Test case for get_comments_by_activity_id

        List Activity Comments  # noqa: E501
        """
        pass

    def test_get_kudoers_by_activity_id(self):
        """Test case for get_kudoers_by_activity_id

        List Activity Kudoers  # noqa: E501
        """
        pass

    def test_get_laps_by_activity_id(self):
        """Test case for get_laps_by_activity_id

        List Activity Laps  # noqa: E501
        """
        pass

    def test_get_logged_in_athlete_activities(self):
        """Test case for get_logged_in_athlete_activities

        List Athlete Activities  # noqa: E501
        """
        pass

    def test_get_zones_by_activity_id(self):
        """Test case for get_zones_by_activity_id

        Get Activity Zones  # noqa: E501
        """
        pass

    def test_update_activity_by_id(self):
        """Test case for update_activity_by_id

        Update Activity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
