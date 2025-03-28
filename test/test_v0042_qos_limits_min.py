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

from slurmrestpy.models.v0042_qos_limits_min import V0042QosLimitsMin


class TestV0042QosLimitsMin(unittest.TestCase):
    """V0042QosLimitsMin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042QosLimitsMin:
        """Test V0042QosLimitsMin
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042QosLimitsMin`
        """
        model = V0042QosLimitsMin()
        if include_optional:
            return V0042QosLimitsMin(
                priority_threshold = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                tres = slurmrestpy.models.v0_0_42_qos_limits_min_tres.v0_0_42_qos_limits_min_tres(
                    per = slurmrestpy.models.v0_0_42_qos_limits_min_tres_per.v0_0_42_qos_limits_min_tres_per(
                        job = [
                            slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                                type = '',
                                name = '',
                                id = 56,
                                count = 56, )
                            ], ), )
            )
        else:
            return V0042QosLimitsMin(
        )
        """

    def testV0042QosLimitsMin(self):
        """Test V0042QosLimitsMin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
