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

from slurmrestpy.models.v0042_account_short import V0042AccountShort


class TestV0042AccountShort(unittest.TestCase):
    """V0042AccountShort unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042AccountShort:
        """Test V0042AccountShort
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042AccountShort`
        """
        model = V0042AccountShort()
        if include_optional:
            return V0042AccountShort(
                description = '',
                organization = ''
            )
        else:
            return V0042AccountShort(
        )
        """

    def testV0042AccountShort(self):
        """Test V0042AccountShort"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
