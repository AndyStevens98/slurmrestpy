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

from slurmrestpy.models.v0042_accounting import V0042Accounting


class TestV0042Accounting(unittest.TestCase):
    """V0042Accounting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042Accounting:
        """Test V0042Accounting
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042Accounting`
        """
        model = V0042Accounting()
        if include_optional:
            return V0042Accounting(
                allocated = slurmrestpy.models.v0_0_42_accounting_allocated.v0_0_42_accounting_allocated(
                    seconds = 56, ),
                id = 56,
                id_alt = 56,
                start = 56,
                tres = slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                    type = '',
                    name = '',
                    id = 56,
                    count = 56, )
            )
        else:
            return V0042Accounting(
        )
        """

    def testV0042Accounting(self):
        """Test V0042Accounting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
