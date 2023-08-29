# coding: utf-8

# flake8: noqa

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from strava_python.api.activities_api import ActivitiesApi
from strava_python.api.athletes_api import AthletesApi
from strava_python.api.clubs_api import ClubsApi
from strava_python.api.gears_api import GearsApi
from strava_python.api.routes_api import RoutesApi
from strava_python.api.segment_efforts_api import SegmentEffortsApi
from strava_python.api.segments_api import SegmentsApi
from strava_python.api.streams_api import StreamsApi
from strava_python.api.uploads_api import UploadsApi

# import ApiClient
from strava_python.api_client import ApiClient
from strava_python.configuration import Configuration
# import models into sdk package
from strava_python.models.activity_stats import ActivityStats
from strava_python.models.activity_total import ActivityTotal
from strava_python.models.activity_type import ActivityType
from strava_python.models.activity_zone import ActivityZone
from strava_python.models.altitude_stream import AltitudeStream
from strava_python.models.base_stream import BaseStream
from strava_python.models.cadence_stream import CadenceStream
from strava_python.models.club_activity import ClubActivity
from strava_python.models.club_athlete import ClubAthlete
from strava_python.models.comment import Comment
from strava_python.models.detailed_activity import DetailedActivity
from strava_python.models.detailed_athlete import DetailedAthlete
from strava_python.models.detailed_club import DetailedClub
from strava_python.models.detailed_gear import DetailedGear
from strava_python.models.detailed_segment import DetailedSegment
from strava_python.models.detailed_segment_effort import DetailedSegmentEffort
from strava_python.models.distance_stream import DistanceStream
from strava_python.models.error import Error
from strava_python.models.explorer_response import ExplorerResponse
from strava_python.models.explorer_segment import ExplorerSegment
from strava_python.models.fault import Fault
from strava_python.models.heart_rate_zone_ranges import HeartRateZoneRanges
from strava_python.models.heartrate_stream import HeartrateStream
from strava_python.models.lap import Lap
from strava_python.models.lat_lng import LatLng
from strava_python.models.lat_lng_stream import LatLngStream
from strava_python.models.meta_activity import MetaActivity
from strava_python.models.meta_athlete import MetaAthlete
from strava_python.models.meta_club import MetaClub
from strava_python.models.moving_stream import MovingStream
from strava_python.models.photos_summary import PhotosSummary
from strava_python.models.photos_summary_primary import PhotosSummaryPrimary
from strava_python.models.polyline_map import PolylineMap
from strava_python.models.power_stream import PowerStream
from strava_python.models.power_zone_ranges import PowerZoneRanges
from strava_python.models.route import Route
from strava_python.models.smooth_grade_stream import SmoothGradeStream
from strava_python.models.smooth_velocity_stream import SmoothVelocityStream
from strava_python.models.split import Split
from strava_python.models.sport_type import SportType
from strava_python.models.stream_set import StreamSet
from strava_python.models.summary_activity import SummaryActivity
from strava_python.models.summary_athlete import SummaryAthlete
from strava_python.models.summary_club import SummaryClub
from strava_python.models.summary_gear import SummaryGear
from strava_python.models.summary_pr_segment_effort import SummaryPRSegmentEffort
from strava_python.models.summary_segment import SummarySegment
from strava_python.models.summary_segment_effort import SummarySegmentEffort
from strava_python.models.temperature_stream import TemperatureStream
from strava_python.models.time_stream import TimeStream
from strava_python.models.timed_zone_distribution import TimedZoneDistribution
from strava_python.models.timed_zone_range import TimedZoneRange
from strava_python.models.updatable_activity import UpdatableActivity
from strava_python.models.upload import Upload
from strava_python.models.zone_range import ZoneRange
from strava_python.models.zone_ranges import ZoneRanges
from strava_python.models.zones import Zones
