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

from slurmrestpy.models.v0040_step_statistics import V0040StepStatistics


class TestV0040StepStatistics(unittest.TestCase):
    """V0040StepStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StepStatistics:
        """Test V0040StepStatistics
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040StepStatistics`
        """
        model = V0040StepStatistics()
        if include_optional:
            return V0040StepStatistics(
                cpu = slurmrestpy.models.v0_0_42_step_statistics_cpu.v0_0_42_step_statistics_CPU(
                    actual_frequency = 56, ),
                energy = slurmrestpy.models.v0_0_40_step_statistics_energy.v0_0_40_step_statistics_energy(
                    consumed = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ), )
            )
        else:
            return V0040StepStatistics(
        )
        """

    def testV0040StepStatistics(self):
        """Test V0040StepStatistics"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
