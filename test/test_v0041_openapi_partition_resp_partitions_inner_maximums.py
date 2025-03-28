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

from slurmrestpy.models.v0041_openapi_partition_resp_partitions_inner_maximums import (
    V0041OpenapiPartitionRespPartitionsInnerMaximums,
)


class TestV0041OpenapiPartitionRespPartitionsInnerMaximums(unittest.TestCase):
    """V0041OpenapiPartitionRespPartitionsInnerMaximums unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiPartitionRespPartitionsInnerMaximums:
        """Test V0041OpenapiPartitionRespPartitionsInnerMaximums
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiPartitionRespPartitionsInnerMaximums`
        """
        model = V0041OpenapiPartitionRespPartitionsInnerMaximums()
        if include_optional:
            return V0041OpenapiPartitionRespPartitionsInnerMaximums(
                cpus_per_node = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_cpus_per_node.v0_0_41_openapi_partition_resp_partitions_inner_maximums_cpus_per_node(
                    set = True,
                    infinite = True,
                    number = 56, ),
                cpus_per_socket = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_cpus_per_socket.v0_0_41_openapi_partition_resp_partitions_inner_maximums_cpus_per_socket(
                    set = True,
                    infinite = True,
                    number = 56, ),
                memory_per_cpu = 56,
                partition_memory_per_cpu = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_cpu.v0_0_41_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_cpu(
                    set = True,
                    infinite = True,
                    number = 56, ),
                partition_memory_per_node = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node.v0_0_41_openapi_partition_resp_partitions_inner_maximums_partition_memory_per_node(
                    set = True,
                    infinite = True,
                    number = 56, ),
                nodes = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_nodes.v0_0_41_openapi_partition_resp_partitions_inner_maximums_nodes(
                    set = True,
                    infinite = True,
                    number = 56, ),
                shares = 56,
                oversubscribe = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_oversubscribe.v0_0_41_openapi_partition_resp_partitions_inner_maximums_oversubscribe(
                    jobs = 56,
                    flags = [
                        'force'
                        ], ),
                time = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_time.v0_0_41_openapi_partition_resp_partitions_inner_maximums_time(
                    set = True,
                    infinite = True,
                    number = 56, ),
                over_time_limit = slurmrestpy.models.v0_0_41_openapi_partition_resp_partitions_inner_maximums_over_time_limit.v0_0_41_openapi_partition_resp_partitions_inner_maximums_over_time_limit(
                    set = True,
                    infinite = True,
                    number = 56, )
            )
        else:
            return V0041OpenapiPartitionRespPartitionsInnerMaximums(
        )
        """

    def testV0041OpenapiPartitionRespPartitionsInnerMaximums(self):
        """Test V0041OpenapiPartitionRespPartitionsInnerMaximums"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
