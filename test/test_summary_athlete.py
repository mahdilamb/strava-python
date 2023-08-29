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
from strava_python.models.summary_athlete import SummaryAthlete  # noqa: E501
from strava_python.rest import ApiException

class TestSummaryAthlete(unittest.TestCase):
    """SummaryAthlete unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SummaryAthlete
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SummaryAthlete`
        """
        model = strava_python.models.summary_athlete.SummaryAthlete()  # noqa: E501
        if include_optional :
            return SummaryAthlete(
                id = 56, 
                resource_state = 56, 
                firstname = '', 
                lastname = '', 
                profile_medium = '', 
                profile = '', 
                city = '', 
                state = '', 
                country = '', 
                sex = 'M', 
                premium = True, 
                summit = True, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return SummaryAthlete(
        )
        """

    def testSummaryAthlete(self):
        """Test SummaryAthlete"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
