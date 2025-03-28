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

from slurmrestpy.models.v0040_acct_gather_energy import V0040AcctGatherEnergy


class TestV0040AcctGatherEnergy(unittest.TestCase):
    """V0040AcctGatherEnergy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AcctGatherEnergy:
        """Test V0040AcctGatherEnergy
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040AcctGatherEnergy`
        """
        model = V0040AcctGatherEnergy()
        if include_optional:
            return V0040AcctGatherEnergy(
                average_watts = 56,
                base_consumed_energy = 56,
                consumed_energy = 56,
                current_watts = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                    set = True,
                    infinite = True,
                    number = 56, ),
                previous_consumed_energy = 56,
                last_collected = 56
            )
        else:
            return V0040AcctGatherEnergy(
        )
        """

    def testV0040AcctGatherEnergy(self):
        """Test V0040AcctGatherEnergy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
