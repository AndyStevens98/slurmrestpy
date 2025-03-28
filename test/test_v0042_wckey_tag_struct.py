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

from slurmrestpy.models.v0042_wckey_tag_struct import V0042WckeyTagStruct


class TestV0042WckeyTagStruct(unittest.TestCase):
    """V0042WckeyTagStruct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042WckeyTagStruct:
        """Test V0042WckeyTagStruct
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042WckeyTagStruct`
        """
        model = V0042WckeyTagStruct()
        if include_optional:
            return V0042WckeyTagStruct(
                wckey = '',
                flags = [
                    'ASSIGNED_DEFAULT'
                    ]
            )
        else:
            return V0042WckeyTagStruct(
                wckey = '',
                flags = [
                    'ASSIGNED_DEFAULT'
                    ],
        )
        """

    def testV0042WckeyTagStruct(self):
        """Test V0042WckeyTagStruct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
