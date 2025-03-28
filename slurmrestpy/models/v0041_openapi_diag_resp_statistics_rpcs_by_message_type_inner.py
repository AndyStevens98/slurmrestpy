# coding: utf-8

"""
Slurm REST API

API to access and control Slurm

The version of the OpenAPI document: Slurm-24.11.1&openapi/slurmdbd&openapi/slurmctld
Contact: sales@schedmd.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Dict, List, Optional, Set

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Self

from slurmrestpy.models.v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time import (
    V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime,
)


class V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner(BaseModel):
    """
    RPCs by type
    """  # noqa: E501

    type_id: StrictInt = Field(description="Message type as integer")
    message_type: StrictStr = Field(description="Message type as string")
    count: StrictInt = Field(description="Number of RPCs received")
    queued: StrictInt = Field(description="Number of RPCs queued")
    dropped: StrictInt = Field(description="Number of RPCs dropped")
    cycle_last: StrictInt = Field(
        description="Number of RPCs processed within the last RPC queue cycle"
    )
    cycle_max: StrictInt = Field(
        description="Maximum number of RPCs processed within a RPC queue cycle since start"
    )
    total_time: StrictInt = Field(
        description="Total time spent processing RPC in seconds"
    )
    average_time: V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime
    __properties: ClassVar[List[str]] = [
        "type_id",
        "message_type",
        "count",
        "queued",
        "dropped",
        "cycle_last",
        "cycle_max",
        "total_time",
        "average_time",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of average_time
        if self.average_time:
            _dict["average_time"] = self.average_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type_id": obj.get("type_id"),
                "message_type": obj.get("message_type"),
                "count": obj.get("count"),
                "queued": obj.get("queued"),
                "dropped": obj.get("dropped"),
                "cycle_last": obj.get("cycle_last"),
                "cycle_max": obj.get("cycle_max"),
                "total_time": obj.get("total_time"),
                "average_time": V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInnerAverageTime.from_dict(
                    obj["average_time"]
                )
                if obj.get("average_time") is not None
                else None,
            }
        )
        return _obj
