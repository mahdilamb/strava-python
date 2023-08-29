# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class Split(BaseModel):
    """
    Split
    """
    average_speed: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The average speed of this split, in meters per second")
    distance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The distance of this split, in meters")
    elapsed_time: Optional[StrictInt] = Field(None, description="The elapsed time of this split, in seconds")
    elevation_difference: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The elevation difference of this split, in meters")
    pace_zone: Optional[StrictInt] = Field(None, description="The pacing zone of this split")
    moving_time: Optional[StrictInt] = Field(None, description="The moving time of this split, in seconds")
    split: Optional[StrictInt] = Field(None, description="N/A")
    __properties = ["average_speed", "distance", "elapsed_time", "elevation_difference", "pace_zone", "moving_time", "split"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Split:
        """Create an instance of Split from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Split:
        """Create an instance of Split from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Split.parse_obj(obj)

        _obj = Split.parse_obj({
            "average_speed": obj.get("average_speed"),
            "distance": obj.get("distance"),
            "elapsed_time": obj.get("elapsed_time"),
            "elevation_difference": obj.get("elevation_difference"),
            "pace_zone": obj.get("pace_zone"),
            "moving_time": obj.get("moving_time"),
            "split": obj.get("split")
        })
        return _obj


