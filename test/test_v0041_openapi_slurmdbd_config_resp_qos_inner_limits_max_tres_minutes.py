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

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes import (
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes,
)


class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes(
                per = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_tres_minutes_per(
                    qos = [
                        slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    job = [
                        slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    account = [

                        ],
                    user = [

                        ], )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxTresMinutes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
