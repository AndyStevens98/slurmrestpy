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

from slurmrestpy.models.v0042_openapi_partition_resp import V0042OpenapiPartitionResp


class TestV0042OpenapiPartitionResp(unittest.TestCase):
    """V0042OpenapiPartitionResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiPartitionResp:
        """Test V0042OpenapiPartitionResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042OpenapiPartitionResp`
        """
        model = V0042OpenapiPartitionResp()
        if include_optional:
            return V0042OpenapiPartitionResp(
                partitions = [
                    slurmrestpy.models.v0/0/42_partition_info.v0.0.42_partition_info(
                        nodes = slurmrestpy.models.v0_0_42_partition_info_nodes.v0_0_42_partition_info_nodes(
                            allowed_allocation = '',
                            configured = '',
                            total = 56, ),
                        accounts = slurmrestpy.models.v0_0_42_partition_info_accounts.v0_0_42_partition_info_accounts(
                            allowed = '',
                            deny = '', ),
                        groups = slurmrestpy.models.v0_0_42_partition_info_groups.v0_0_42_partition_info_groups(
                            allowed = '', ),
                        qos = slurmrestpy.models.v0_0_42_partition_info_qos.v0_0_42_partition_info_qos(
                            allowed = '',
                            deny = '',
                            assigned = '', ),
                        alternate = '',
                        tres = slurmrestpy.models.v0_0_42_partition_info_tres.v0_0_42_partition_info_tres(
                            billing_weights = '',
                            configured = '', ),
                        cluster = '',
                        select_type = [
                            'CPU'
                            ],
                        cpus = slurmrestpy.models.v0_0_42_partition_info_cpus.v0_0_42_partition_info_cpus(
                            task_binding = 56,
                            total = 56, ),
                        defaults = slurmrestpy.models.v0_0_42_partition_info_defaults.v0_0_42_partition_info_defaults(
                            memory_per_cpu = 56,
                            partition_memory_per_cpu = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            partition_memory_per_node = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            time = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            job = '', ),
                        grace_time = 56,
                        maximums = slurmrestpy.models.v0_0_42_partition_info_maximums.v0_0_42_partition_info_maximums(
                            cpus_per_node = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            cpus_per_socket = ,
                            memory_per_cpu = 56,
                            shares = 56,
                            oversubscribe = slurmrestpy.models.v0_0_42_partition_info_maximums_oversubscribe.v0_0_42_partition_info_maximums_oversubscribe(
                                jobs = 56,
                                flags = [
                                    'force'
                                    ], ),
                            over_time_limit = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ), ),
                        minimums = slurmrestpy.models.v0_0_42_partition_info_minimums.v0_0_42_partition_info_minimums(),
                        name = '',
                        node_sets = '',
                        priority = slurmrestpy.models.v0_0_42_partition_info_priority.v0_0_42_partition_info_priority(
                            job_factor = 56,
                            tier = 56, ),
                        timeouts = slurmrestpy.models.v0_0_42_partition_info_timeouts.v0_0_42_partition_info_timeouts(
                            resume = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            suspend = , ),
                        partition = slurmrestpy.models.v0_0_42_partition_info_partition.v0_0_42_partition_info_partition(
                            state = [
                                'INACTIVE'
                                ], ),
                        suspend_time = , )
                    ],
                last_update = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                meta = slurmrestpy.models.v0/0/42_openapi_meta.v0.0.42_openapi_meta(
                    plugin = slurmrestpy.models.v0_0_42_openapi_meta_plugin.v0_0_42_openapi_meta_plugin(
                        type = '',
                        name = '',
                        data_parser = '',
                        accounting_storage = '', ),
                    client = slurmrestpy.models.v0_0_42_openapi_meta_client.v0_0_42_openapi_meta_client(
                        source = '',
                        user = '',
                        group = '', ),
                    command = [
                        ''
                        ],
                    slurm = slurmrestpy.models.v0_0_42_openapi_meta_slurm.v0_0_42_openapi_meta_slurm(
                        version = slurmrestpy.models.v0_0_42_openapi_meta_slurm_version.v0_0_42_openapi_meta_slurm_version(
                            major = '',
                            micro = '',
                            minor = '', ),
                        release = '',
                        cluster = '', ), ),
                errors = [
                    slurmrestpy.models.v0/0/42_openapi_error.v0.0.42_openapi_error(
                        description = '',
                        error_number = 56,
                        error = '',
                        source = '', )
                    ],
                warnings = [
                    slurmrestpy.models.v0/0/42_openapi_warning.v0.0.42_openapi_warning(
                        description = '',
                        source = '', )
                    ]
            )
        else:
            return V0042OpenapiPartitionResp(
                partitions = [
                    slurmrestpy.models.v0/0/42_partition_info.v0.0.42_partition_info(
                        nodes = slurmrestpy.models.v0_0_42_partition_info_nodes.v0_0_42_partition_info_nodes(
                            allowed_allocation = '',
                            configured = '',
                            total = 56, ),
                        accounts = slurmrestpy.models.v0_0_42_partition_info_accounts.v0_0_42_partition_info_accounts(
                            allowed = '',
                            deny = '', ),
                        groups = slurmrestpy.models.v0_0_42_partition_info_groups.v0_0_42_partition_info_groups(
                            allowed = '', ),
                        qos = slurmrestpy.models.v0_0_42_partition_info_qos.v0_0_42_partition_info_qos(
                            allowed = '',
                            deny = '',
                            assigned = '', ),
                        alternate = '',
                        tres = slurmrestpy.models.v0_0_42_partition_info_tres.v0_0_42_partition_info_tres(
                            billing_weights = '',
                            configured = '', ),
                        cluster = '',
                        select_type = [
                            'CPU'
                            ],
                        cpus = slurmrestpy.models.v0_0_42_partition_info_cpus.v0_0_42_partition_info_cpus(
                            task_binding = 56,
                            total = 56, ),
                        defaults = slurmrestpy.models.v0_0_42_partition_info_defaults.v0_0_42_partition_info_defaults(
                            memory_per_cpu = 56,
                            partition_memory_per_cpu = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            partition_memory_per_node = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            time = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            job = '', ),
                        grace_time = 56,
                        maximums = slurmrestpy.models.v0_0_42_partition_info_maximums.v0_0_42_partition_info_maximums(
                            cpus_per_node = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            cpus_per_socket = ,
                            memory_per_cpu = 56,
                            shares = 56,
                            oversubscribe = slurmrestpy.models.v0_0_42_partition_info_maximums_oversubscribe.v0_0_42_partition_info_maximums_oversubscribe(
                                jobs = 56,
                                flags = [
                                    'force'
                                    ], ),
                            over_time_limit = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ), ),
                        minimums = slurmrestpy.models.v0_0_42_partition_info_minimums.v0_0_42_partition_info_minimums(),
                        name = '',
                        node_sets = '',
                        priority = slurmrestpy.models.v0_0_42_partition_info_priority.v0_0_42_partition_info_priority(
                            job_factor = 56,
                            tier = 56, ),
                        timeouts = slurmrestpy.models.v0_0_42_partition_info_timeouts.v0_0_42_partition_info_timeouts(
                            resume = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            suspend = , ),
                        partition = slurmrestpy.models.v0_0_42_partition_info_partition.v0_0_42_partition_info_partition(
                            state = [
                                'INACTIVE'
                                ], ),
                        suspend_time = , )
                    ],
                last_update = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
        )
        """

    def testV0042OpenapiPartitionResp(self):
        """Test V0042OpenapiPartitionResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
