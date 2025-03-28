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

from slurmrestpy.models.v0040_partition_info_maximums import V0040PartitionInfoMaximums


class TestV0040PartitionInfoMaximums(unittest.TestCase):
    """V0040PartitionInfoMaximums unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040PartitionInfoMaximums:
        """Test V0040PartitionInfoMaximums
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040PartitionInfoMaximums`
        """
        model = V0040PartitionInfoMaximums()
        if include_optional:
            return V0040PartitionInfoMaximums(
                cpus_per_node = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                cpus_per_socket = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                memory_per_cpu = 56,
                partition_memory_per_cpu = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                partition_memory_per_node = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                nodes = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                shares = 56,
                oversubscribe = slurmrestpy.models.v0_0_40_partition_info_maximums_oversubscribe.v0_0_40_partition_info_maximums_oversubscribe(
                    jobs = 56,
                    flags = [
                        'force'
                        ], ),
                time = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                over_time_limit = slurmrestpy.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                    set = True,
                    infinite = True,
                    number = 56, )
            )
        else:
            return V0040PartitionInfoMaximums(
        )
        """

    def testV0040PartitionInfoMaximums(self):
        """Test V0040PartitionInfoMaximums"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
