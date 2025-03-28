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

from slurmrestpy.models.v0040_assoc_max_tres_minutes import V0040AssocMaxTresMinutes


class TestV0040AssocMaxTresMinutes(unittest.TestCase):
    """V0040AssocMaxTresMinutes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040AssocMaxTresMinutes:
        """Test V0040AssocMaxTresMinutes
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040AssocMaxTresMinutes`
        """
        model = V0040AssocMaxTresMinutes()
        if include_optional:
            return V0040AssocMaxTresMinutes(
                total = [
                    slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                        type = '',
                        name = '',
                        id = 56,
                        count = 56, )
                    ],
                per = slurmrestpy.models.v0_0_40_qos_limits_min_tres_per.v0_0_40_qos_limits_min_tres_per(
                    job = [
                        slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ], )
            )
        else:
            return V0040AssocMaxTresMinutes(
        )
        """

    def testV0040AssocMaxTresMinutes(self):
        """Test V0040AssocMaxTresMinutes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
