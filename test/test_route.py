# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import strava_python
from strava_python.models.route import Route  # noqa: E501
from strava_python.rest import ApiException

class TestRoute(unittest.TestCase):
    """Route unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Route
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Route`
        """
        model = strava_python.models.route.Route()  # noqa: E501
        if include_optional :
            return Route(
                athlete = None, 
                description = '', 
                distance = 1.337, 
                elevation_gain = 1.337, 
                id = 56, 
                id_str = '', 
                map = strava_python.models.polyline_map.PolylineMap(
                    id = '', 
                    polyline = '', 
                    summary_polyline = '', ), 
                name = '', 
                private = True, 
                starred = True, 
                timestamp = 56, 
                type = 56, 
                sub_type = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                estimated_moving_time = 56, 
                segments = [
                    strava_python.models.summary_segment.SummarySegment(
                        id = 56, 
                        name = '', 
                        activity_type = 'Ride', 
                        distance = 1.337, 
                        average_grade = 1.337, 
                        maximum_grade = 1.337, 
                        elevation_high = 1.337, 
                        elevation_low = 1.337, 
                        start_latlng = [
                            1.337
                            ], 
                        end_latlng = [
                            1.337
                            ], 
                        climb_category = 56, 
                        city = '', 
                        state = '', 
                        country = '', 
                        private = True, 
                        athlete_pr_effort = strava_python.models.summary_pr_segment_effort.SummaryPRSegmentEffort(
                            pr_activity_id = 56, 
                            pr_elapsed_time = 56, 
                            pr_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            effort_count = 56, ), 
                        athlete_segment_stats = strava_python.models.summary_segment_effort.SummarySegmentEffort(
                            id = 56, 
                            activity_id = 56, 
                            elapsed_time = 56, 
                            start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            start_date_local = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            distance = 1.337, 
                            is_kom = True, ), )
                    ]
            )
        else :
            return Route(
        )
        """

    def testRoute(self):
        """Test Route"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
