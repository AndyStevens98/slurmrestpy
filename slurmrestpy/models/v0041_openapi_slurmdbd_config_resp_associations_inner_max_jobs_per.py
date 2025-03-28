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

from pydantic import BaseModel, ConfigDict
from typing_extensions import Self

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_submitted import (
    V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPerSubmitted,
)
from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing import (
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing,
)
from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count import (
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount,
)
from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job import (
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob,
)


class V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer(BaseModel):
    """
    V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer
    """  # noqa: E501

    count: Optional[V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount] = (
        None
    )
    accruing: Optional[
        V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing
    ] = None
    submitted: Optional[
        V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPerSubmitted
    ] = None
    wall_clock: Optional[
        V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob
    ] = None
    __properties: ClassVar[List[str]] = ["count", "accruing", "submitted", "wall_clock"]

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
        """Create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of count
        if self.count:
            _dict["count"] = self.count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accruing
        if self.accruing:
            _dict["accruing"] = self.accruing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of submitted
        if self.submitted:
            _dict["submitted"] = self.submitted.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wall_clock
        if self.wall_clock:
            _dict["wall_clock"] = self.wall_clock.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "count": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsCount.from_dict(
                    obj["count"]
                )
                if obj.get("count") is not None
                else None,
                "accruing": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing.from_dict(
                    obj["accruing"]
                )
                if obj.get("accruing") is not None
                else None,
                "submitted": V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsPerSubmitted.from_dict(
                    obj["submitted"]
                )
                if obj.get("submitted") is not None
                else None,
                "wall_clock": V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxWallClockPerJob.from_dict(
                    obj["wall_clock"]
                )
                if obj.get("wall_clock") is not None
                else None,
            }
        )
        return _obj
