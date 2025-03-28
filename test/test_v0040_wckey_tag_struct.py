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

from slurmrestpy.models.v0040_wckey_tag_struct import V0040WckeyTagStruct


class TestV0040WckeyTagStruct(unittest.TestCase):
    """V0040WckeyTagStruct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040WckeyTagStruct:
        """Test V0040WckeyTagStruct
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040WckeyTagStruct`
        """
        model = V0040WckeyTagStruct()
        if include_optional:
            return V0040WckeyTagStruct(
                wckey = '',
                flags = [
                    'ASSIGNED_DEFAULT'
                    ]
            )
        else:
            return V0040WckeyTagStruct(
                wckey = '',
                flags = [
                    'ASSIGNED_DEFAULT'
                    ],
        )
        """

    def testV0040WckeyTagStruct(self):
        """Test V0040WckeyTagStruct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
