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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class Upload(BaseModel):
    """
    Upload
    """
    id: Optional[StrictInt] = Field(None, description="The unique identifier of the upload")
    id_str: Optional[StrictStr] = Field(None, description="The unique identifier of the upload in string format")
    external_id: Optional[StrictStr] = Field(None, description="The external identifier of the upload")
    error: Optional[StrictStr] = Field(None, description="The error associated with this upload")
    status: Optional[StrictStr] = Field(None, description="The status of this upload")
    activity_id: Optional[StrictInt] = Field(None, description="The identifier of the activity this upload resulted into")
    __properties = ["id", "id_str", "external_id", "error", "status", "activity_id"]

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
    def from_json(cls, json_str: str) -> Upload:
        """Create an instance of Upload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Upload:
        """Create an instance of Upload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Upload.parse_obj(obj)

        _obj = Upload.parse_obj({
            "id": obj.get("id"),
            "id_str": obj.get("id_str"),
            "external_id": obj.get("external_id"),
            "error": obj.get("error"),
            "status": obj.get("status"),
            "activity_id": obj.get("activity_id")
        })
        return _obj


