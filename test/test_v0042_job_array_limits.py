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

from slurmrestpy.models.v0042_job_array_limits import V0042JobArrayLimits


class TestV0042JobArrayLimits(unittest.TestCase):
    """V0042JobArrayLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobArrayLimits:
        """Test V0042JobArrayLimits
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042JobArrayLimits`
        """
        model = V0042JobArrayLimits()
        if include_optional:
            return V0042JobArrayLimits(
                max = slurmrestpy.models.v0_0_42_job_array_limits_max.v0_0_42_job_array_limits_max(
                    running = slurmrestpy.models.v0_0_42_job_array_limits_max_running.v0_0_42_job_array_limits_max_running(
                        tasks = 56, ), )
            )
        else:
            return V0042JobArrayLimits(
        )
        """

    def testV0042JobArrayLimits(self):
        """Test V0042JobArrayLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
