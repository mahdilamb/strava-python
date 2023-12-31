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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, conlist
from strava_python.models.zone_range import ZoneRange

class HeartRateZoneRanges(BaseModel):
    """
    HeartRateZoneRanges
    """
    custom_zones: Optional[StrictBool] = Field(None, description="Whether the athlete has set their own custom heart rate zones")
    zones: Optional[conlist(ZoneRange)] = None
    __properties = ["custom_zones", "zones"]

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
    def from_json(cls, json_str: str) -> HeartRateZoneRanges:
        """Create an instance of HeartRateZoneRanges from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in zones (list)
        _items = []
        if self.zones:
            for _item in self.zones:
                if _item:
                    _items.append(_item.to_dict())
            _dict['zones'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HeartRateZoneRanges:
        """Create an instance of HeartRateZoneRanges from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HeartRateZoneRanges.parse_obj(obj)

        _obj = HeartRateZoneRanges.parse_obj({
            "custom_zones": obj.get("custom_zones"),
            "zones": [ZoneRange.from_dict(_item) for _item in obj.get("zones")] if obj.get("zones") is not None else None
        })
        return _obj


