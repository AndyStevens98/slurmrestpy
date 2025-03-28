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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self

from slurmrestpy.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_return_code import (
    V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCodeReturnCode,
)
from slurmrestpy.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal import (
    V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCodeSignal,
)


class V0041OpenapiJobInfoRespJobsInnerExitCode(BaseModel):
    """
    Exit code of the job
    """  # noqa: E501

    status: Optional[List[StrictStr]] = Field(
        default=None, description="Status given by return code"
    )
    return_code: Optional[
        V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCodeReturnCode
    ] = None
    signal: Optional[V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCodeSignal] = None
    __properties: ClassVar[List[str]] = ["status", "return_code", "signal"]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(
                ["INVALID", "PENDING", "SUCCESS", "ERROR", "SIGNALED", "CORE_DUMPED"]
            ):
                raise ValueError(
                    "each list item must be one of ('INVALID', 'PENDING', 'SUCCESS', 'ERROR', 'SIGNALED', 'CORE_DUMPED')"
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
        """Create an instance of V0041OpenapiJobInfoRespJobsInnerExitCode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of return_code
        if self.return_code:
            _dict["return_code"] = self.return_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signal
        if self.signal:
            _dict["signal"] = self.signal.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiJobInfoRespJobsInnerExitCode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "status": obj.get("status"),
                "return_code": V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCodeReturnCode.from_dict(
                    obj["return_code"]
                )
                if obj.get("return_code") is not None
                else None,
                "signal": V0041OpenapiSlurmdbdJobsRespJobsInnerDerivedExitCodeSignal.from_dict(
                    obj["signal"]
                )
                if obj.get("signal") is not None
                else None,
            }
        )
        return _obj
