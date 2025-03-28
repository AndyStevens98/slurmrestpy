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

from slurmrestpy.models.v0040_shares_resp_msg import V0040SharesRespMsg


class TestV0040SharesRespMsg(unittest.TestCase):
    """V0040SharesRespMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040SharesRespMsg:
        """Test V0040SharesRespMsg
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040SharesRespMsg`
        """
        model = V0040SharesRespMsg()
        if include_optional:
            return V0040SharesRespMsg(
                shares = [
                    slurmrestpy.models.v0/0/40_assoc_shares_obj_wrap.v0.0.40_assoc_shares_obj_wrap(
                        id = 56,
                        cluster = '',
                        name = '',
                        parent = '',
                        partition = '',
                        shares_normalized = slurmrestpy.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                            set = True,
                            infinite = True,
                            number = 1.337, ),
                        shares = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        tres = slurmrestpy.models.v0_0_40_assoc_shares_obj_wrap_tres.v0_0_40_assoc_shares_obj_wrap_tres(
                            run_seconds = [
                                slurmrestpy.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                    name = '',
                                    value = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                                        set = True,
                                        infinite = True,
                                        number = 56, ), )
                                ],
                            group_minutes = [
                                slurmrestpy.models.v0/0/40_shares_uint64_tres.v0.0.40_shares_uint64_tres(
                                    name = '', )
                                ],
                            usage = [
                                slurmrestpy.models.v0/0/40_shares_float128_tres.v0.0.40_shares_float128_tres(
                                    name = '', )
                                ], ),
                        effective_usage = 1.337,
                        usage_normalized = slurmrestpy.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                            set = True,
                            infinite = True,
                            number = 1.337, ),
                        usage = 56,
                        fairshare = slurmrestpy.models.v0_0_40_assoc_shares_obj_wrap_fairshare.v0_0_40_assoc_shares_obj_wrap_fairshare(
                            factor = 1.337,
                            level = 1.337, ),
                        type = [
                            'USER'
                            ], )
                    ],
                total_shares = 56
            )
        else:
            return V0040SharesRespMsg(
        )
        """

    def testV0040SharesRespMsg(self):
        """Test V0040SharesRespMsg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
