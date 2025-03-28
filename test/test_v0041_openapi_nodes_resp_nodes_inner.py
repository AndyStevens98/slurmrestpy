# coding: utf-8

"""
Slurm REST API

API to access and control Slurm

The version of the OpenAPI document: Slurm-24.11.1&openapi/slurmdbd&openapi/slurmctld
Contact: sales@schedmd.com
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from slurmrestpy.models.v0041_openapi_nodes_resp_nodes_inner import (
    V0041OpenapiNodesRespNodesInner,
)


class TestV0041OpenapiNodesRespNodesInner(unittest.TestCase):
    """V0041OpenapiNodesRespNodesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiNodesRespNodesInner:
        """Test V0041OpenapiNodesRespNodesInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiNodesRespNodesInner`
        """
        model = V0041OpenapiNodesRespNodesInner()
        if include_optional:
            return V0041OpenapiNodesRespNodesInner(
                architecture = '',
                burstbuffer_network_address = '',
                boards = 56,
                boot_time = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_boot_time.v0_0_41_openapi_nodes_resp_nodes_inner_boot_time(
                    set = True,
                    infinite = True,
                    number = 56, ),
                cluster_name = '',
                cores = 56,
                specialized_cores = 56,
                cpu_binding = 56,
                cpu_load = 56,
                free_mem = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_free_mem.v0_0_41_openapi_nodes_resp_nodes_inner_free_mem(
                    set = True,
                    infinite = True,
                    number = 56, ),
                cpus = 56,
                effective_cpus = 56,
                specialized_cpus = '',
                energy = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_energy.v0_0_41_openapi_nodes_resp_nodes_inner_energy(
                    average_watts = 56,
                    base_consumed_energy = 56,
                    consumed_energy = 56,
                    current_watts = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_energy_current_watts.v0_0_41_openapi_nodes_resp_nodes_inner_energy_current_watts(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    previous_consumed_energy = 56,
                    last_collected = 56, ),
                external_sensors = slurmrestpy.models.external_sensors.external_sensors(),
                extra = '',
                power = slurmrestpy.models.power.power(),
                features = [
                    ''
                    ],
                active_features = [
                    ''
                    ],
                gpu_spec = '',
                gres = '',
                gres_drained = '',
                gres_used = '',
                instance_id = '',
                instance_type = '',
                last_busy = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_last_busy.v0_0_41_openapi_nodes_resp_nodes_inner_last_busy(
                    set = True,
                    infinite = True,
                    number = 56, ),
                mcs_label = '',
                specialized_memory = 56,
                name = '',
                next_state_after_reboot = [
                    'INVALID'
                    ],
                address = '',
                hostname = '',
                state = [
                    'INVALID'
                    ],
                operating_system = '',
                owner = '',
                partitions = [
                    ''
                    ],
                port = 56,
                real_memory = 56,
                res_cores_per_gpu = 56,
                comment = '',
                reason = '',
                reason_changed_at = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_reason_changed_at.v0_0_41_openapi_nodes_resp_nodes_inner_reason_changed_at(
                    set = True,
                    infinite = True,
                    number = 56, ),
                reason_set_by_user = '',
                resume_after = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_resume_after.v0_0_41_openapi_nodes_resp_nodes_inner_resume_after(
                    set = True,
                    infinite = True,
                    number = 56, ),
                reservation = '',
                alloc_memory = 56,
                alloc_cpus = 56,
                alloc_idle_cpus = 56,
                tres_used = '',
                tres_weighted = 1.337,
                slurmd_start_time = slurmrestpy.models.v0_0_41_openapi_nodes_resp_nodes_inner_slurmd_start_time.v0_0_41_openapi_nodes_resp_nodes_inner_slurmd_start_time(
                    set = True,
                    infinite = True,
                    number = 56, ),
                sockets = 56,
                threads = 56,
                temporary_disk = 56,
                weight = 56,
                tres = '',
                version = ''
            )
        else:
            return V0041OpenapiNodesRespNodesInner(
        )
        """

    def testV0041OpenapiNodesRespNodesInner(self):
        """Test V0041OpenapiNodesRespNodesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
