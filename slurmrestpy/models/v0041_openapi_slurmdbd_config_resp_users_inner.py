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

from slurmrestpy.models.v0040_user_default import V0040UserDefault
from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_accounts_inner_associations_inner import (
    V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner,
)
from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_accounts_inner_coordinators_inner import (
    V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner,
)
from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner import (
    V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner,
)


class V0041OpenapiSlurmdbdConfigRespUsersInner(BaseModel):
    """
    V0041OpenapiSlurmdbdConfigRespUsersInner
    """  # noqa: E501

    administrator_level: Optional[List[StrictStr]] = Field(
        default=None, description="AdminLevel granted to the user"
    )
    associations: Optional[
        List[V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner]
    ] = Field(default=None, description="Associations created for this user")
    coordinators: Optional[
        List[V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner]
    ] = Field(default=None, description="Accounts this user is a coordinator for")
    default: Optional[V0040UserDefault] = None
    flags: Optional[List[StrictStr]] = Field(
        default=None, description="Flags associated with user"
    )
    name: StrictStr = Field(description="User name")
    old_name: Optional[StrictStr] = Field(
        default=None, description="Previous user name"
    )
    wckeys: Optional[List[V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner]] = Field(
        default=None, description="List of available WCKeys"
    )
    __properties: ClassVar[List[str]] = [
        "administrator_level",
        "associations",
        "coordinators",
        "default",
        "flags",
        "name",
        "old_name",
        "wckeys",
    ]

    @field_validator("administrator_level")
    def administrator_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(["Not Set", "None", "Operator", "Administrator"]):
                raise ValueError(
                    "each list item must be one of ('Not Set', 'None', 'Operator', 'Administrator')"
                )
        return value

    @field_validator("flags")
    def flags_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(["NONE", "DELETED"]):
                raise ValueError("each list item must be one of ('NONE', 'DELETED')")
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
        """Create an instance of V0041OpenapiSlurmdbdConfigRespUsersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in coordinators (list)
        _items = []
        if self.coordinators:
            for _item_coordinators in self.coordinators:
                if _item_coordinators:
                    _items.append(_item_coordinators.to_dict())
            _dict["coordinators"] = _items
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict["default"] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in wckeys (list)
        _items = []
        if self.wckeys:
            for _item_wckeys in self.wckeys:
                if _item_wckeys:
                    _items.append(_item_wckeys.to_dict())
            _dict["wckeys"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0041OpenapiSlurmdbdConfigRespUsersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "administrator_level": obj.get("administrator_level"),
                "associations": [
                    V0041OpenapiSlurmdbdConfigRespAccountsInnerAssociationsInner.from_dict(
                        _item
                    )
                    for _item in obj["associations"]
                ]
                if obj.get("associations") is not None
                else None,
                "coordinators": [
                    V0041OpenapiSlurmdbdConfigRespAccountsInnerCoordinatorsInner.from_dict(
                        _item
                    )
                    for _item in obj["coordinators"]
                ]
                if obj.get("coordinators") is not None
                else None,
                "default": V0040UserDefault.from_dict(obj["default"])
                if obj.get("default") is not None
                else None,
                "flags": obj.get("flags"),
                "name": obj.get("name"),
                "old_name": obj.get("old_name"),
                "wckeys": [
                    V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner.from_dict(_item)
                    for _item in obj["wckeys"]
                ]
                if obj.get("wckeys") is not None
                else None,
            }
        )
        return _obj
