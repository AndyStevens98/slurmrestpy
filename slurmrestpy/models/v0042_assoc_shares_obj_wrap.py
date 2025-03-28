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

from slurmrestpy.models.v0042_assoc_shares_obj_wrap_fairshare import (
    V0042AssocSharesObjWrapFairshare,
)
from slurmrestpy.models.v0042_assoc_shares_obj_wrap_tres import (
    V0042AssocSharesObjWrapTres,
)
from slurmrestpy.models.v0042_float64_no_val_struct import V0042Float64NoValStruct
from slurmrestpy.models.v0042_uint32_no_val_struct import V0042Uint32NoValStruct


class V0042AssocSharesObjWrap(BaseModel):
    """
    V0042AssocSharesObjWrap
    """  # noqa: E501

    id: Optional[StrictInt] = Field(default=None, description="Association ID")
    cluster: Optional[StrictStr] = Field(default=None, description="Cluster name")
    name: Optional[StrictStr] = Field(default=None, description="Share name")
    parent: Optional[StrictStr] = Field(default=None, description="Parent name")
    partition: Optional[StrictStr] = Field(default=None, description="Partition name")
    shares_normalized: Optional[V0042Float64NoValStruct] = None
    shares: Optional[V0042Uint32NoValStruct] = None
    tres: Optional[V0042AssocSharesObjWrapTres] = None
    effective_usage: Optional[V0042Float64NoValStruct] = None
    usage_normalized: Optional[V0042Float64NoValStruct] = None
    usage: Optional[StrictInt] = Field(
        default=None, description="Measure of tresbillableunits usage"
    )
    fairshare: Optional[V0042AssocSharesObjWrapFairshare] = None
    type: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = [
        "id",
        "cluster",
        "name",
        "parent",
        "partition",
        "shares_normalized",
        "shares",
        "tres",
        "effective_usage",
        "usage_normalized",
        "usage",
        "fairshare",
        "type",
    ]

    @field_validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(["USER", "ASSOCIATION"]):
                raise ValueError(
                    "each list item must be one of ('USER', 'ASSOCIATION')"
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
        """Create an instance of V0042AssocSharesObjWrap from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shares_normalized
        if self.shares_normalized:
            _dict["shares_normalized"] = self.shares_normalized.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shares
        if self.shares:
            _dict["shares"] = self.shares.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tres
        if self.tres:
            _dict["tres"] = self.tres.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective_usage
        if self.effective_usage:
            _dict["effective_usage"] = self.effective_usage.to_dict()
        # override the default output from pydantic by calling `to_dict()` of usage_normalized
        if self.usage_normalized:
            _dict["usage_normalized"] = self.usage_normalized.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fairshare
        if self.fairshare:
            _dict["fairshare"] = self.fairshare.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042AssocSharesObjWrap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "cluster": obj.get("cluster"),
                "name": obj.get("name"),
                "parent": obj.get("parent"),
                "partition": obj.get("partition"),
                "shares_normalized": V0042Float64NoValStruct.from_dict(
                    obj["shares_normalized"]
                )
                if obj.get("shares_normalized") is not None
                else None,
                "shares": V0042Uint32NoValStruct.from_dict(obj["shares"])
                if obj.get("shares") is not None
                else None,
                "tres": V0042AssocSharesObjWrapTres.from_dict(obj["tres"])
                if obj.get("tres") is not None
                else None,
                "effective_usage": V0042Float64NoValStruct.from_dict(
                    obj["effective_usage"]
                )
                if obj.get("effective_usage") is not None
                else None,
                "usage_normalized": V0042Float64NoValStruct.from_dict(
                    obj["usage_normalized"]
                )
                if obj.get("usage_normalized") is not None
                else None,
                "usage": obj.get("usage"),
                "fairshare": V0042AssocSharesObjWrapFairshare.from_dict(
                    obj["fairshare"]
                )
                if obj.get("fairshare") is not None
                else None,
                "type": obj.get("type"),
            }
        )
        return _obj
