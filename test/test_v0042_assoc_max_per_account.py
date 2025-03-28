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

from slurmrestpy.models.v0042_assoc_max_per_account import V0042AssocMaxPerAccount


class TestV0042AssocMaxPerAccount(unittest.TestCase):
    """V0042AssocMaxPerAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042AssocMaxPerAccount:
        """Test V0042AssocMaxPerAccount
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042AssocMaxPerAccount`
        """
        model = V0042AssocMaxPerAccount()
        if include_optional:
            return V0042AssocMaxPerAccount(
                wall_clock = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, )
            )
        else:
            return V0042AssocMaxPerAccount(
        )
        """

    def testV0042AssocMaxPerAccount(self):
        """Test V0042AssocMaxPerAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
