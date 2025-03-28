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

from slurmrestpy.models.v0042_job_time_system import V0042JobTimeSystem


class TestV0042JobTimeSystem(unittest.TestCase):
    """V0042JobTimeSystem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobTimeSystem:
        """Test V0042JobTimeSystem
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042JobTimeSystem`
        """
        model = V0042JobTimeSystem()
        if include_optional:
            return V0042JobTimeSystem(
                seconds = 56,
                microseconds = 56
            )
        else:
            return V0042JobTimeSystem(
        )
        """

    def testV0042JobTimeSystem(self):
        """Test V0042JobTimeSystem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
