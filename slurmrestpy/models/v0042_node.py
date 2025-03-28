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
from typing import Any, ClassVar, Dict, List, Optional, Set, Union

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    StrictStr,
    field_validator,
)
from typing_extensions import Self

from slurmrestpy.models.v0042_acct_gather_energy import V0042AcctGatherEnergy
from slurmrestpy.models.v0042_uint64_no_val_struct import V0042Uint64NoValStruct


class V0042Node(BaseModel):
    """
    V0042Node
    """  # noqa: E501

    architecture: Optional[StrictStr] = Field(
        default=None, description="Computer architecture"
    )
    burstbuffer_network_address: Optional[StrictStr] = Field(
        default=None,
        description="Alternate network path to be used for sbcast network traffic",
    )
    boards: Optional[StrictInt] = Field(
        default=None,
        description="Number of Baseboards in nodes with a baseboard controller",
    )
    boot_time: Optional[V0042Uint64NoValStruct] = None
    cluster_name: Optional[StrictStr] = Field(
        default=None, description="Cluster name (only set in federated environments)"
    )
    cores: Optional[StrictInt] = Field(
        default=None,
        description="Number of cores in a single physical processor socket",
    )
    specialized_cores: Optional[StrictInt] = Field(
        default=None, description="Number of cores reserved for system use"
    )
    cpu_binding: Optional[StrictInt] = Field(
        default=None, description="Default method for binding tasks to allocated CPUs"
    )
    cpu_load: Optional[StrictInt] = Field(
        default=None, description="CPU load as reported by the OS"
    )
    free_mem: Optional[V0042Uint64NoValStruct] = None
    cpus: Optional[StrictInt] = Field(
        default=None, description="Total CPUs, including cores and threads"
    )
    effective_cpus: Optional[StrictInt] = Field(
        default=None,
        description="Number of effective CPUs (excluding specialized CPUs)",
    )
    specialized_cpus: Optional[StrictStr] = Field(
        default=None,
        description="Abstract CPU IDs on this node reserved for exclusive use by slurmd and slurmstepd",
    )
    energy: Optional[V0042AcctGatherEnergy] = None
    external_sensors: Optional[Dict[str, Any]] = None
    extra: Optional[StrictStr] = Field(
        default=None,
        description="Arbitrary string used for node filtering if extra constraints are enabled",
    )
    power: Optional[Dict[str, Any]] = None
    features: Optional[List[StrictStr]] = None
    active_features: Optional[List[StrictStr]] = None
    gpu_spec: Optional[StrictStr] = Field(
        default=None, description="CPU cores reserved for jobs that also use a GPU"
    )
    gres: Optional[StrictStr] = Field(default=None, description="Generic resources")
    gres_drained: Optional[StrictStr] = Field(
        default=None, description="Drained generic resources"
    )
    gres_used: Optional[StrictStr] = Field(
        default=None, description="Generic resources currently in use"
    )
    instance_id: Optional[StrictStr] = Field(
        default=None, description="Cloud instance ID"
    )
    instance_type: Optional[StrictStr] = Field(
        default=None, description="Cloud instance type"
    )
    last_busy: Optional[V0042Uint64NoValStruct] = None
    mcs_label: Optional[StrictStr] = Field(
        default=None, description="Multi-Category Security label"
    )
    specialized_memory: Optional[StrictInt] = Field(
        default=None,
        description="Combined memory limit, in MB, for Slurm compute node daemons",
    )
    name: Optional[StrictStr] = Field(default=None, description="NodeName")
    next_state_after_reboot: Optional[List[StrictStr]] = None
    address: Optional[StrictStr] = Field(
        default=None, description="NodeAddr, used to establish a communication path"
    )
    hostname: Optional[StrictStr] = Field(default=None, description="NodeHostname")
    state: Optional[List[StrictStr]] = None
    operating_system: Optional[StrictStr] = Field(
        default=None, description="Operating system reported by the node"
    )
    owner: Optional[StrictStr] = Field(
        default=None,
        description="User allowed to run jobs on this node (unset if no restriction)",
    )
    partitions: Optional[List[StrictStr]] = None
    port: Optional[StrictInt] = Field(
        default=None, description="TCP port number of the slurmd"
    )
    real_memory: Optional[StrictInt] = Field(
        default=None, description="Total memory in MB on the node"
    )
    res_cores_per_gpu: Optional[StrictInt] = Field(
        default=None, description="Number of CPU cores per GPU restricted to GPU jobs"
    )
    comment: Optional[StrictStr] = Field(default=None, description="Arbitrary comment")
    reason: Optional[StrictStr] = Field(
        default=None,
        description='Describes why the node is in a "DOWN", "DRAINED", "DRAINING", "FAILING" or "FAIL" state',
    )
    reason_changed_at: Optional[V0042Uint64NoValStruct] = None
    reason_set_by_user: Optional[StrictStr] = Field(
        default=None, description="User who set the reason"
    )
    resume_after: Optional[V0042Uint64NoValStruct] = None
    reservation: Optional[StrictStr] = Field(
        default=None, description="Name of reservation containing this node"
    )
    alloc_memory: Optional[StrictInt] = Field(
        default=None, description="Total memory in MB currently allocated for jobs"
    )
    alloc_cpus: Optional[StrictInt] = Field(
        default=None, description="Total number of CPUs currently allocated for jobs"
    )
    alloc_idle_cpus: Optional[StrictInt] = Field(
        default=None, description="Total number of idle CPUs"
    )
    tres_used: Optional[StrictStr] = Field(
        default=None, description="Trackable resources currently allocated for jobs"
    )
    tres_weighted: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Weighted number of billable trackable resources allocated",
    )
    slurmd_start_time: Optional[V0042Uint64NoValStruct] = None
    sockets: Optional[StrictInt] = Field(
        default=None,
        description="Number of physical processor sockets/chips on the node",
    )
    threads: Optional[StrictInt] = Field(
        default=None, description="Number of logical threads in a single physical core"
    )
    temporary_disk: Optional[StrictInt] = Field(
        default=None, description="Total size in MB of temporary disk storage in TmpFS"
    )
    weight: Optional[StrictInt] = Field(
        default=None, description="Weight of the node for scheduling purposes"
    )
    tres: Optional[StrictStr] = Field(
        default=None, description="Configured trackable resources"
    )
    version: Optional[StrictStr] = Field(default=None, description="Slurmd version")
    __properties: ClassVar[List[str]] = [
        "architecture",
        "burstbuffer_network_address",
        "boards",
        "boot_time",
        "cluster_name",
        "cores",
        "specialized_cores",
        "cpu_binding",
        "cpu_load",
        "free_mem",
        "cpus",
        "effective_cpus",
        "specialized_cpus",
        "energy",
        "external_sensors",
        "extra",
        "power",
        "features",
        "active_features",
        "gpu_spec",
        "gres",
        "gres_drained",
        "gres_used",
        "instance_id",
        "instance_type",
        "last_busy",
        "mcs_label",
        "specialized_memory",
        "name",
        "next_state_after_reboot",
        "address",
        "hostname",
        "state",
        "operating_system",
        "owner",
        "partitions",
        "port",
        "real_memory",
        "res_cores_per_gpu",
        "comment",
        "reason",
        "reason_changed_at",
        "reason_set_by_user",
        "resume_after",
        "reservation",
        "alloc_memory",
        "alloc_cpus",
        "alloc_idle_cpus",
        "tres_used",
        "tres_weighted",
        "slurmd_start_time",
        "sockets",
        "threads",
        "temporary_disk",
        "weight",
        "tres",
        "version",
    ]

    @field_validator("next_state_after_reboot")
    def next_state_after_reboot_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(
                [
                    "INVALID",
                    "UNKNOWN",
                    "DOWN",
                    "IDLE",
                    "ALLOCATED",
                    "ERROR",
                    "MIXED",
                    "FUTURE",
                    "RESERVED",
                    "UNDRAIN",
                    "CLOUD",
                    "RESUME",
                    "DRAIN",
                    "COMPLETING",
                    "NOT_RESPONDING",
                    "POWERED_DOWN",
                    "FAIL",
                    "POWERING_UP",
                    "MAINTENANCE",
                    "REBOOT_REQUESTED",
                    "REBOOT_CANCELED",
                    "POWERING_DOWN",
                    "DYNAMIC_FUTURE",
                    "REBOOT_ISSUED",
                    "PLANNED",
                    "INVALID_REG",
                    "POWER_DOWN",
                    "POWER_UP",
                    "POWER_DRAIN",
                    "DYNAMIC_NORM",
                ]
            ):
                raise ValueError(
                    "each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')"
                )
        return value

    @field_validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(
                [
                    "INVALID",
                    "UNKNOWN",
                    "DOWN",
                    "IDLE",
                    "ALLOCATED",
                    "ERROR",
                    "MIXED",
                    "FUTURE",
                    "RESERVED",
                    "UNDRAIN",
                    "CLOUD",
                    "RESUME",
                    "DRAIN",
                    "COMPLETING",
                    "NOT_RESPONDING",
                    "POWERED_DOWN",
                    "FAIL",
                    "POWERING_UP",
                    "MAINTENANCE",
                    "REBOOT_REQUESTED",
                    "REBOOT_CANCELED",
                    "POWERING_DOWN",
                    "DYNAMIC_FUTURE",
                    "REBOOT_ISSUED",
                    "PLANNED",
                    "INVALID_REG",
                    "POWER_DOWN",
                    "POWER_UP",
                    "POWER_DRAIN",
                    "DYNAMIC_NORM",
                ]
            ):
                raise ValueError(
                    "each list item must be one of ('INVALID', 'UNKNOWN', 'DOWN', 'IDLE', 'ALLOCATED', 'ERROR', 'MIXED', 'FUTURE', 'RESERVED', 'UNDRAIN', 'CLOUD', 'RESUME', 'DRAIN', 'COMPLETING', 'NOT_RESPONDING', 'POWERED_DOWN', 'FAIL', 'POWERING_UP', 'MAINTENANCE', 'REBOOT_REQUESTED', 'REBOOT_CANCELED', 'POWERING_DOWN', 'DYNAMIC_FUTURE', 'REBOOT_ISSUED', 'PLANNED', 'INVALID_REG', 'POWER_DOWN', 'POWER_UP', 'POWER_DRAIN', 'DYNAMIC_NORM')"
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
        """Create an instance of V0042Node from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of boot_time
        if self.boot_time:
            _dict["boot_time"] = self.boot_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of free_mem
        if self.free_mem:
            _dict["free_mem"] = self.free_mem.to_dict()
        # override the default output from pydantic by calling `to_dict()` of energy
        if self.energy:
            _dict["energy"] = self.energy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_busy
        if self.last_busy:
            _dict["last_busy"] = self.last_busy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reason_changed_at
        if self.reason_changed_at:
            _dict["reason_changed_at"] = self.reason_changed_at.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resume_after
        if self.resume_after:
            _dict["resume_after"] = self.resume_after.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slurmd_start_time
        if self.slurmd_start_time:
            _dict["slurmd_start_time"] = self.slurmd_start_time.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of V0042Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "architecture": obj.get("architecture"),
                "burstbuffer_network_address": obj.get("burstbuffer_network_address"),
                "boards": obj.get("boards"),
                "boot_time": V0042Uint64NoValStruct.from_dict(obj["boot_time"])
                if obj.get("boot_time") is not None
                else None,
                "cluster_name": obj.get("cluster_name"),
                "cores": obj.get("cores"),
                "specialized_cores": obj.get("specialized_cores"),
                "cpu_binding": obj.get("cpu_binding"),
                "cpu_load": obj.get("cpu_load"),
                "free_mem": V0042Uint64NoValStruct.from_dict(obj["free_mem"])
                if obj.get("free_mem") is not None
                else None,
                "cpus": obj.get("cpus"),
                "effective_cpus": obj.get("effective_cpus"),
                "specialized_cpus": obj.get("specialized_cpus"),
                "energy": V0042AcctGatherEnergy.from_dict(obj["energy"])
                if obj.get("energy") is not None
                else None,
                "external_sensors": obj.get("external_sensors"),
                "extra": obj.get("extra"),
                "power": obj.get("power"),
                "features": obj.get("features"),
                "active_features": obj.get("active_features"),
                "gpu_spec": obj.get("gpu_spec"),
                "gres": obj.get("gres"),
                "gres_drained": obj.get("gres_drained"),
                "gres_used": obj.get("gres_used"),
                "instance_id": obj.get("instance_id"),
                "instance_type": obj.get("instance_type"),
                "last_busy": V0042Uint64NoValStruct.from_dict(obj["last_busy"])
                if obj.get("last_busy") is not None
                else None,
                "mcs_label": obj.get("mcs_label"),
                "specialized_memory": obj.get("specialized_memory"),
                "name": obj.get("name"),
                "next_state_after_reboot": obj.get("next_state_after_reboot"),
                "address": obj.get("address"),
                "hostname": obj.get("hostname"),
                "state": obj.get("state"),
                "operating_system": obj.get("operating_system"),
                "owner": obj.get("owner"),
                "partitions": obj.get("partitions"),
                "port": obj.get("port"),
                "real_memory": obj.get("real_memory"),
                "res_cores_per_gpu": obj.get("res_cores_per_gpu"),
                "comment": obj.get("comment"),
                "reason": obj.get("reason"),
                "reason_changed_at": V0042Uint64NoValStruct.from_dict(
                    obj["reason_changed_at"]
                )
                if obj.get("reason_changed_at") is not None
                else None,
                "reason_set_by_user": obj.get("reason_set_by_user"),
                "resume_after": V0042Uint64NoValStruct.from_dict(obj["resume_after"])
                if obj.get("resume_after") is not None
                else None,
                "reservation": obj.get("reservation"),
                "alloc_memory": obj.get("alloc_memory"),
                "alloc_cpus": obj.get("alloc_cpus"),
                "alloc_idle_cpus": obj.get("alloc_idle_cpus"),
                "tres_used": obj.get("tres_used"),
                "tres_weighted": obj.get("tres_weighted"),
                "slurmd_start_time": V0042Uint64NoValStruct.from_dict(
                    obj["slurmd_start_time"]
                )
                if obj.get("slurmd_start_time") is not None
                else None,
                "sockets": obj.get("sockets"),
                "threads": obj.get("threads"),
                "temporary_disk": obj.get("temporary_disk"),
                "weight": obj.get("weight"),
                "tres": obj.get("tres"),
                "version": obj.get("version"),
            }
        )
        return _obj
