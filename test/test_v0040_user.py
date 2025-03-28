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

from slurmrestpy.models.v0040_user import V0040User


class TestV0040User(unittest.TestCase):
    """V0040User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040User:
        """Test V0040User
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040User`
        """
        model = V0040User()
        if include_optional:
            return V0040User(
                administrator_level = [
                    'Not Set'
                    ],
                associations = [
                    slurmrestpy.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                        account = '',
                        cluster = '',
                        partition = '',
                        user = '',
                        id = 56, )
                    ],
                coordinators = [
                    slurmrestpy.models.v0/0/40_coord.v0.0.40_coord(
                        name = '',
                        direct = True, )
                    ],
                default = slurmrestpy.models.v0_0_40_user_default.v0_0_40_user_default(
                    account = '',
                    wckey = '', ),
                flags = [
                    'NONE'
                    ],
                name = '',
                old_name = '',
                wckeys = [
                    slurmrestpy.models.v0/0/40_wckey.v0.0.40_wckey(
                        accounting = [
                            slurmrestpy.models.v0/0/40_accounting.v0.0.40_accounting(
                                allocated = slurmrestpy.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                                    seconds = 56, ),
                                id = 56,
                                start = 56,
                                tres = slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '',
                                    name = '',
                                    id = 56,
                                    count = 56, ), )
                            ],
                        cluster = '',
                        id = 56,
                        name = '',
                        user = '',
                        flags = [
                            'DELETED'
                            ], )
                    ]
            )
        else:
            return V0040User(
                name = '',
        )
        """

    def testV0040User(self):
        """Test V0040User"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
