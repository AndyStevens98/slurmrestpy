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

from slurmrestpy.models.v0040_assoc_max_jobs_per import V0040AssocMaxJobsPer
from slurmrestpy.models.v0040_uint32_no_val import V0040Uint32NoVal


class V0040AssocMaxJobs(BaseModel):
    """
    V0040AssocMaxJobs
    """  # noqa: E501

    per: Optional[V0040AssocMaxJobsPer] = None
    active: Optional[V0040Uint32NoVal] = None
    accruing: Optional[V0040Uint32NoVal] = None
    total: Optional[V0040Uint32NoVal] = None
    __properties: ClassVar[List[str]] = ["per", "active", "accruing", "total"]

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
        """Create an instance of V0040AssocMaxJobs from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of per
        if self.per:
            _dict["per"] = self.per.to_dict()
        # override the default output from pydantic by calling `to_dict()` of active
        if self.active:
            _dict["active"] = self.active.to_dict()
        # override the default output from pydantic by calling `to_dict()` of accruing
        if self.accruing:
            _dict["accruing"] = self.accruing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total
        if self.total:
            _dict["total"] = self.total.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040AssocMaxJobs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "per": V0040AssocMaxJobsPer.from_dict(obj["per"])
                if obj.get("per") is not None
                else None,
                "active": V0040Uint32NoVal.from_dict(obj["active"])
                if obj.get("active") is not None
                else None,
                "accruing": V0040Uint32NoVal.from_dict(obj["accruing"])
                if obj.get("accruing") is not None
                else None,
                "total": V0040Uint32NoVal.from_dict(obj["total"])
                if obj.get("total") is not None
                else None,
            }
        )
        return _obj
