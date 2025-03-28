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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing_extensions import Self

from slurmrestpy.models.v0040_partition_info_maximums_oversubscribe import (
    V0040PartitionInfoMaximumsOversubscribe,
)
from slurmrestpy.models.v0040_uint16_no_val import V0040Uint16NoVal
from slurmrestpy.models.v0040_uint32_no_val import V0040Uint32NoVal
from slurmrestpy.models.v0040_uint64_no_val import V0040Uint64NoVal


class V0040PartitionInfoMaximums(BaseModel):
    """
    V0040PartitionInfoMaximums
    """  # noqa: E501

    cpus_per_node: Optional[V0040Uint32NoVal] = None
    cpus_per_socket: Optional[V0040Uint32NoVal] = None
    memory_per_cpu: Optional[StrictInt] = Field(
        default=None, description="MaxMemPerCPU or MaxMemPerNode"
    )
    partition_memory_per_cpu: Optional[V0040Uint64NoVal] = None
    partition_memory_per_node: Optional[V0040Uint64NoVal] = None
    nodes: Optional[V0040Uint32NoVal] = None
    shares: Optional[StrictInt] = Field(default=None, description="OverSubscribe")
    oversubscribe: Optional[V0040PartitionInfoMaximumsOversubscribe] = None
    time: Optional[V0040Uint32NoVal] = None
    over_time_limit: Optional[V0040Uint16NoVal] = None
    __properties: ClassVar[List[str]] = [
        "cpus_per_node",
        "cpus_per_socket",
        "memory_per_cpu",
        "partition_memory_per_cpu",
        "partition_memory_per_node",
        "nodes",
        "shares",
        "oversubscribe",
        "time",
        "over_time_limit",
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
        """Create an instance of V0040PartitionInfoMaximums from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cpus_per_node
        if self.cpus_per_node:
            _dict["cpus_per_node"] = self.cpus_per_node.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpus_per_socket
        if self.cpus_per_socket:
            _dict["cpus_per_socket"] = self.cpus_per_socket.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partition_memory_per_cpu
        if self.partition_memory_per_cpu:
            _dict["partition_memory_per_cpu"] = self.partition_memory_per_cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partition_memory_per_node
        if self.partition_memory_per_node:
            _dict["partition_memory_per_node"] = (
                self.partition_memory_per_node.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of nodes
        if self.nodes:
            _dict["nodes"] = self.nodes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oversubscribe
        if self.oversubscribe:
            _dict["oversubscribe"] = self.oversubscribe.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time
        if self.time:
            _dict["time"] = self.time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of over_time_limit
        if self.over_time_limit:
            _dict["over_time_limit"] = self.over_time_limit.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0040PartitionInfoMaximums from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "cpus_per_node": V0040Uint32NoVal.from_dict(obj["cpus_per_node"])
                if obj.get("cpus_per_node") is not None
                else None,
                "cpus_per_socket": V0040Uint32NoVal.from_dict(obj["cpus_per_socket"])
                if obj.get("cpus_per_socket") is not None
                else None,
                "memory_per_cpu": obj.get("memory_per_cpu"),
                "partition_memory_per_cpu": V0040Uint64NoVal.from_dict(
                    obj["partition_memory_per_cpu"]
                )
                if obj.get("partition_memory_per_cpu") is not None
                else None,
                "partition_memory_per_node": V0040Uint64NoVal.from_dict(
                    obj["partition_memory_per_node"]
                )
                if obj.get("partition_memory_per_node") is not None
                else None,
                "nodes": V0040Uint32NoVal.from_dict(obj["nodes"])
                if obj.get("nodes") is not None
                else None,
                "shares": obj.get("shares"),
                "oversubscribe": V0040PartitionInfoMaximumsOversubscribe.from_dict(
                    obj["oversubscribe"]
                )
                if obj.get("oversubscribe") is not None
                else None,
                "time": V0040Uint32NoVal.from_dict(obj["time"])
                if obj.get("time") is not None
                else None,
                "over_time_limit": V0040Uint16NoVal.from_dict(obj["over_time_limit"])
                if obj.get("over_time_limit") is not None
                else None,
            }
        )
        return _obj
