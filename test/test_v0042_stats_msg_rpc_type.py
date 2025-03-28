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

from slurmrestpy.models.v0042_stats_msg_rpc_type import V0042StatsMsgRpcType


class TestV0042StatsMsgRpcType(unittest.TestCase):
    """V0042StatsMsgRpcType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042StatsMsgRpcType:
        """Test V0042StatsMsgRpcType
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042StatsMsgRpcType`
        """
        model = V0042StatsMsgRpcType()
        if include_optional:
            return V0042StatsMsgRpcType(
                type_id = 56,
                message_type = '',
                count = 56,
                queued = 56,
                dropped = 56,
                cycle_last = 56,
                cycle_max = 56,
                total_time = 56,
                average_time = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, )
            )
        else:
            return V0042StatsMsgRpcType(
                type_id = 56,
                message_type = '',
                count = 56,
                queued = 56,
                dropped = 56,
                cycle_last = 56,
                cycle_max = 56,
                total_time = 56,
                average_time = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
        )
        """

    def testV0042StatsMsgRpcType(self):
        """Test V0042StatsMsgRpcType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
