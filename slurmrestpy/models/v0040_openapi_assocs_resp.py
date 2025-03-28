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

from slurmrestpy.models.v0040_assoc import V0040Assoc
from slurmrestpy.models.v0040_openapi_error import V0040OpenapiError
from slurmrestpy.models.v0040_openapi_meta import V0040OpenapiMeta
from slurmrestpy.models.v0040_openapi_warning import V0040OpenapiWarning


class V0040OpenapiAssocsResp(BaseModel):
    """
    V0040OpenapiAssocsResp
    """  # noqa: E501

    associations: List[V0040Assoc]
    meta: Optional[V0040OpenapiMeta] = None
    errors: Optional[List[V0040OpenapiError]] = None
    warnings: Optional[List[V0040OpenapiWarning]] = None
    __properties: ClassVar[List[str]] = ["associations", "meta", "errors", "warnings"]

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
        """Create an instance of V0040OpenapiAssocsResp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in associations (list)
        _items = []
        if self.associations:
            for _item_associations in self.associations:
                if _item_associations:
                    _items.append(_item_associations.to_dict())
            _dict["associations"] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict["meta"] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict["errors"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict["warnings"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040OpenapiAssocsResp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "associations": [
                    V0040Assoc.from_dict(_item) for _item in obj["associations"]
                ]
                if obj.get("associations") is not None
                else None,
                "meta": V0040OpenapiMeta.from_dict(obj["meta"])
                if obj.get("meta") is not None
                else None,
                "errors": [
                    V0040OpenapiError.from_dict(_item) for _item in obj["errors"]
                ]
                if obj.get("errors") is not None
                else None,
                "warnings": [
                    V0040OpenapiWarning.from_dict(_item) for _item in obj["warnings"]
                ]
                if obj.get("warnings") is not None
                else None,
            }
        )
        return _obj
