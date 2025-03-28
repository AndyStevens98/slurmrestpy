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

from slurmrestpy.models.v0042_bf_exit_fields import V0042BfExitFields


class TestV0042BfExitFields(unittest.TestCase):
    """V0042BfExitFields unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042BfExitFields:
        """Test V0042BfExitFields
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042BfExitFields`
        """
        model = V0042BfExitFields()
        if include_optional:
            return V0042BfExitFields(
                end_job_queue = 56,
                bf_max_job_start = 56,
                bf_max_job_test = 56,
                bf_max_time = 56,
                bf_node_space_size = 56,
                state_changed = 56
            )
        else:
            return V0042BfExitFields(
        )
        """

    def testV0042BfExitFields(self):
        """Test V0042BfExitFields"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
