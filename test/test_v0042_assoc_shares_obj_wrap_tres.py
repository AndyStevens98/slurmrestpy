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

from slurmrestpy.models.v0042_assoc_shares_obj_wrap_tres import (
    V0042AssocSharesObjWrapTres,
)


class TestV0042AssocSharesObjWrapTres(unittest.TestCase):
    """V0042AssocSharesObjWrapTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042AssocSharesObjWrapTres:
        """Test V0042AssocSharesObjWrapTres
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042AssocSharesObjWrapTres`
        """
        model = V0042AssocSharesObjWrapTres()
        if include_optional:
            return V0042AssocSharesObjWrapTres(
                run_seconds = [
                    slurmrestpy.models.v0/0/42_shares_uint64_tres.v0.0.42_shares_uint64_tres(
                        name = '',
                        value = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                            set = True,
                            infinite = True,
                            number = 56, ), )
                    ],
                group_minutes = [
                    slurmrestpy.models.v0/0/42_shares_uint64_tres.v0.0.42_shares_uint64_tres(
                        name = '',
                        value = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                            set = True,
                            infinite = True,
                            number = 56, ), )
                    ],
                usage = [
                    slurmrestpy.models.v0/0/42_shares_float128_tres.v0.0.42_shares_float128_tres(
                        name = '',
                        value = 1.337, )
                    ]
            )
        else:
            return V0042AssocSharesObjWrapTres(
        )
        """

    def testV0042AssocSharesObjWrapTres(self):
        """Test V0042AssocSharesObjWrapTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
