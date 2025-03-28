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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing_extensions import Self

from slurmrestpy.models.v0042_reservation_core_spec import V0042ReservationCoreSpec
from slurmrestpy.models.v0042_reservation_info_purge_completed import (
    V0042ReservationInfoPurgeCompleted,
)
from slurmrestpy.models.v0042_uint32_no_val_struct import V0042Uint32NoValStruct
from slurmrestpy.models.v0042_uint64_no_val_struct import V0042Uint64NoValStruct


class V0042ReservationInfo(BaseModel):
    """
    V0042ReservationInfo
    """  # noqa: E501

    accounts: Optional[StrictStr] = Field(
        default=None, description="Comma separated list of permitted accounts"
    )
    burst_buffer: Optional[StrictStr] = Field(default=None, description="BurstBuffer")
    core_count: Optional[StrictInt] = Field(default=None, description="CoreCnt")
    core_specializations: Optional[List[V0042ReservationCoreSpec]] = None
    end_time: Optional[V0042Uint64NoValStruct] = None
    features: Optional[StrictStr] = Field(default=None, description="Features")
    flags: Optional[List[StrictStr]] = None
    groups: Optional[StrictStr] = Field(default=None, description="Groups")
    licenses: Optional[StrictStr] = Field(default=None, description="Licenses")
    max_start_delay: Optional[StrictInt] = Field(
        default=None, description="MaxStartDelay in seconds"
    )
    name: Optional[StrictStr] = Field(default=None, description="ReservationName")
    node_count: Optional[StrictInt] = Field(default=None, description="NodeCnt")
    node_list: Optional[StrictStr] = Field(default=None, description="Nodes")
    partition: Optional[StrictStr] = Field(default=None, description="PartitionName")
    purge_completed: Optional[V0042ReservationInfoPurgeCompleted] = None
    start_time: Optional[V0042Uint64NoValStruct] = None
    watts: Optional[V0042Uint32NoValStruct] = None
    tres: Optional[StrictStr] = Field(
        default=None, description="Comma separated list of required TRES"
    )
    users: Optional[StrictStr] = Field(
        default=None, description="Comma separated list of permitted users"
    )
    __properties: ClassVar[List[str]] = [
        "accounts",
        "burst_buffer",
        "core_count",
        "core_specializations",
        "end_time",
        "features",
        "flags",
        "groups",
        "licenses",
        "max_start_delay",
        "name",
        "node_count",
        "node_list",
        "partition",
        "purge_completed",
        "start_time",
        "watts",
        "tres",
        "users",
    ]

    @field_validator("flags")
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(
                [
                    "MAINT",
                    "NO_MAINT",
                    "DAILY",
                    "NO_DAILY",
                    "WEEKLY",
                    "NO_WEEKLY",
                    "IGNORE_JOBS",
                    "NO_IGNORE_JOBS",
                    "ANY_NODES",
                    "STATIC",
                    "NO_STATIC",
                    "PART_NODES",
                    "NO_PART_NODES",
                    "OVERLAP",
                    "SPEC_NODES",
                    "TIME_FLOAT",
                    "REPLACE",
                    "ALL_NODES",
                    "PURGE_COMP",
                    "WEEKDAY",
                    "NO_WEEKDAY",
                    "WEEKEND",
                    "NO_WEEKEND",
                    "FLEX",
                    "NO_FLEX",
                    "DURATION_PLUS",
                    "DURATION_MINUS",
                    "NO_HOLD_JOBS_AFTER_END",
                    "NO_PURGE_COMP",
                    "MAGNETIC",
                    "SKIP",
                    "HOURLY",
                    "NO_HOURLY",
                    "USER_DELETE",
                    "NO_USER_DELETE",
                    "REOCCURRING",
                ]
            ):
                raise ValueError(
                    "each list item must be one of ('MAINT', 'NO_MAINT', 'DAILY', 'NO_DAILY', 'WEEKLY', 'NO_WEEKLY', 'IGNORE_JOBS', 'NO_IGNORE_JOBS', 'ANY_NODES', 'STATIC', 'NO_STATIC', 'PART_NODES', 'NO_PART_NODES', 'OVERLAP', 'SPEC_NODES', 'TIME_FLOAT', 'REPLACE', 'ALL_NODES', 'PURGE_COMP', 'WEEKDAY', 'NO_WEEKDAY', 'WEEKEND', 'NO_WEEKEND', 'FLEX', 'NO_FLEX', 'DURATION_PLUS', 'DURATION_MINUS', 'NO_HOLD_JOBS_AFTER_END', 'NO_PURGE_COMP', 'MAGNETIC', 'SKIP', 'HOURLY', 'NO_HOURLY', 'USER_DELETE', 'NO_USER_DELETE', 'REOCCURRING')"
                )
        return value

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
        """Create an instance of V0042ReservationInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in core_specializations (list)
        _items = []
        if self.core_specializations:
            for _item_core_specializations in self.core_specializations:
                if _item_core_specializations:
                    _items.append(_item_core_specializations.to_dict())
            _dict["core_specializations"] = _items
        # override the default output from pydantic by calling `to_dict()` of end_time
        if self.end_time:
            _dict["end_time"] = self.end_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of purge_completed
        if self.purge_completed:
            _dict["purge_completed"] = self.purge_completed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of start_time
        if self.start_time:
            _dict["start_time"] = self.start_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of watts
        if self.watts:
            _dict["watts"] = self.watts.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042ReservationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "accounts": obj.get("accounts"),
                "burst_buffer": obj.get("burst_buffer"),
                "core_count": obj.get("core_count"),
                "core_specializations": [
                    V0042ReservationCoreSpec.from_dict(_item)
                    for _item in obj["core_specializations"]
                ]
                if obj.get("core_specializations") is not None
                else None,
                "end_time": V0042Uint64NoValStruct.from_dict(obj["end_time"])
                if obj.get("end_time") is not None
                else None,
                "features": obj.get("features"),
                "flags": obj.get("flags"),
                "groups": obj.get("groups"),
                "licenses": obj.get("licenses"),
                "max_start_delay": obj.get("max_start_delay"),
                "name": obj.get("name"),
                "node_count": obj.get("node_count"),
                "node_list": obj.get("node_list"),
                "partition": obj.get("partition"),
                "purge_completed": V0042ReservationInfoPurgeCompleted.from_dict(
                    obj["purge_completed"]
                )
                if obj.get("purge_completed") is not None
                else None,
                "start_time": V0042Uint64NoValStruct.from_dict(obj["start_time"])
                if obj.get("start_time") is not None
                else None,
                "watts": V0042Uint32NoValStruct.from_dict(obj["watts"])
                if obj.get("watts") is not None
                else None,
                "tres": obj.get("tres"),
                "users": obj.get("users"),
            }
        )
        return _obj
