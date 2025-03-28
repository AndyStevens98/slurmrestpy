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


class V0040JobSubmitResponseMsg(BaseModel):
    """
    V0040JobSubmitResponseMsg
    """  # noqa: E501

    job_id: Optional[StrictInt] = Field(default=None, description="New job ID")
    step_id: Optional[StrictStr] = Field(default=None, description="New job step ID")
    error_code: Optional[StrictInt] = Field(default=None, description="Error code")
    error: Optional[StrictStr] = Field(default=None, description="Error message")
    job_submit_user_msg: Optional[StrictStr] = Field(
        default=None, description="Message to user from job_submit plugin"
    )
    __properties: ClassVar[List[str]] = [
        "job_id",
        "step_id",
        "error_code",
        "error",
        "job_submit_user_msg",
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
        """Create an instance of V0040JobSubmitResponseMsg from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040JobSubmitResponseMsg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "job_id": obj.get("job_id"),
                "step_id": obj.get("step_id"),
                "error_code": obj.get("error_code"),
                "error": obj.get("error"),
                "job_submit_user_msg": obj.get("job_submit_user_msg"),
            }
        )
        return _obj
