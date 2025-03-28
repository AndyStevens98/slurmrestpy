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

from slurmrestpy.models.v0042_partition_info_priority import V0042PartitionInfoPriority


class TestV0042PartitionInfoPriority(unittest.TestCase):
    """V0042PartitionInfoPriority unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042PartitionInfoPriority:
        """Test V0042PartitionInfoPriority
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042PartitionInfoPriority`
        """
        model = V0042PartitionInfoPriority()
        if include_optional:
            return V0042PartitionInfoPriority(
                job_factor = 56,
                tier = 56
            )
        else:
            return V0042PartitionInfoPriority(
        )
        """

    def testV0042PartitionInfoPriority(self):
        """Test V0042PartitionInfoPriority"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
