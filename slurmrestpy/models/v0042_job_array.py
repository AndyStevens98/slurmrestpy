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

from slurmrestpy.models.v0042_job_array_limits import V0042JobArrayLimits
from slurmrestpy.models.v0042_uint32_no_val_struct import V0042Uint32NoValStruct


class V0042JobArray(BaseModel):
    """
    V0042JobArray
    """  # noqa: E501

    job_id: Optional[StrictInt] = Field(
        default=None, description="Job ID of job array, or 0 if N/A"
    )
    limits: Optional[V0042JobArrayLimits] = None
    task_id: Optional[V0042Uint32NoValStruct] = None
    task: Optional[StrictStr] = Field(
        default=None, description="String expression of task IDs in this record"
    )
    __properties: ClassVar[List[str]] = ["job_id", "limits", "task_id", "task"]

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
        """Create an instance of V0042JobArray from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of limits
        if self.limits:
            _dict["limits"] = self.limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of task_id
        if self.task_id:
            _dict["task_id"] = self.task_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042JobArray from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "job_id": obj.get("job_id"),
                "limits": V0042JobArrayLimits.from_dict(obj["limits"])
                if obj.get("limits") is not None
                else None,
                "task_id": V0042Uint32NoValStruct.from_dict(obj["task_id"])
                if obj.get("task_id") is not None
                else None,
                "task": obj.get("task"),
            }
        )
        return _obj
