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

from slurmrestpy.models.v0042_assoc_max_tres_group import V0042AssocMaxTresGroup
from slurmrestpy.models.v0042_assoc_max_tres_minutes import V0042AssocMaxTresMinutes
from slurmrestpy.models.v0042_assoc_max_tres_per import V0042AssocMaxTresPer
from slurmrestpy.models.v0042_tres import V0042Tres


class V0042AssocMaxTres(BaseModel):
    """
    V0042AssocMaxTres
    """  # noqa: E501

    total: Optional[List[V0042Tres]] = None
    group: Optional[V0042AssocMaxTresGroup] = None
    minutes: Optional[V0042AssocMaxTresMinutes] = None
    per: Optional[V0042AssocMaxTresPer] = None
    __properties: ClassVar[List[str]] = ["total", "group", "minutes", "per"]

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
        """Create an instance of V0042AssocMaxTres from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in total (list)
        _items = []
        if self.total:
            for _item_total in self.total:
                if _item_total:
                    _items.append(_item_total.to_dict())
            _dict["total"] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict["group"] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of minutes
        if self.minutes:
            _dict["minutes"] = self.minutes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of per
        if self.per:
            _dict["per"] = self.per.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042AssocMaxTres from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "total": [V0042Tres.from_dict(_item) for _item in obj["total"]]
                if obj.get("total") is not None
                else None,
                "group": V0042AssocMaxTresGroup.from_dict(obj["group"])
                if obj.get("group") is not None
                else None,
                "minutes": V0042AssocMaxTresMinutes.from_dict(obj["minutes"])
                if obj.get("minutes") is not None
                else None,
                "per": V0042AssocMaxTresPer.from_dict(obj["per"])
                if obj.get("per") is not None
                else None,
            }
        )
        return _obj
