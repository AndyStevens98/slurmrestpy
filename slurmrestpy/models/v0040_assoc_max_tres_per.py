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

from slurmrestpy.models.v0040_tres import V0040Tres


class V0040AssocMaxTresPer(BaseModel):
    """
    V0040AssocMaxTresPer
    """  # noqa: E501

    job: Optional[List[V0040Tres]] = None
    node: Optional[List[V0040Tres]] = None
    __properties: ClassVar[List[str]] = ["job", "node"]

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
        """Create an instance of V0040AssocMaxTresPer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in job (list)
        _items = []
        if self.job:
            for _item_job in self.job:
                if _item_job:
                    _items.append(_item_job.to_dict())
            _dict["job"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in node (list)
        _items = []
        if self.node:
            for _item_node in self.node:
                if _item_node:
                    _items.append(_item_node.to_dict())
            _dict["node"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040AssocMaxTresPer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "job": [V0040Tres.from_dict(_item) for _item in obj["job"]]
                if obj.get("job") is not None
                else None,
                "node": [V0040Tres.from_dict(_item) for _item in obj["node"]]
                if obj.get("node") is not None
                else None,
            }
        )
        return _obj
