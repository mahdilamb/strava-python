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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conint, conlist, validator

class ExplorerSegment(BaseModel):
    """
    ExplorerSegment
    """
    id: Optional[StrictInt] = Field(None, description="The unique identifier of this segment")
    name: Optional[StrictStr] = Field(None, description="The name of this segment")
    climb_category: Optional[conint(strict=True, le=5, ge=0)] = Field(None, description="The category of the climb [0, 5]. Higher is harder ie. 5 is Hors catégorie, 0 is uncategorized in climb_category. If climb_category = 5, climb_category_desc = HC. If climb_category = 2, climb_category_desc = 3.")
    climb_category_desc: Optional[StrictStr] = Field(None, description="The description for the category of the climb")
    avg_grade: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The segment's average grade, in percents")
    start_latlng: Optional[conlist(Union[StrictFloat, StrictInt], max_items=2, min_items=2)] = Field(None, description="A pair of latitude/longitude coordinates, represented as an array of 2 floating point numbers.")
    end_latlng: Optional[conlist(Union[StrictFloat, StrictInt], max_items=2, min_items=2)] = Field(None, description="A pair of latitude/longitude coordinates, represented as an array of 2 floating point numbers.")
    elev_difference: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The segments's evelation difference, in meters")
    distance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The segment's distance, in meters")
    points: Optional[StrictStr] = Field(None, description="The polyline of the segment")
    __properties = ["id", "name", "climb_category", "climb_category_desc", "avg_grade", "start_latlng", "end_latlng", "elev_difference", "distance", "points"]

    @validator('climb_category_desc')
    def climb_category_desc_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('NC', '4', '3', '2', '1', 'HC'):
            raise ValueError("must be one of enum values ('NC', '4', '3', '2', '1', 'HC')")
        return value

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
    def from_json(cls, json_str: str) -> ExplorerSegment:
        """Create an instance of ExplorerSegment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExplorerSegment:
        """Create an instance of ExplorerSegment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExplorerSegment.parse_obj(obj)

        _obj = ExplorerSegment.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "climb_category": obj.get("climb_category"),
            "climb_category_desc": obj.get("climb_category_desc"),
            "avg_grade": obj.get("avg_grade"),
            "start_latlng": obj.get("start_latlng"),
            "end_latlng": obj.get("end_latlng"),
            "elev_difference": obj.get("elev_difference"),
            "distance": obj.get("distance"),
            "points": obj.get("points")
        })
        return _obj


