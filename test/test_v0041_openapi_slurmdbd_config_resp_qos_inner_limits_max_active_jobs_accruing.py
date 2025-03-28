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

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing import (
    V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing,
)


class TestV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing(
    unittest.TestCase
):
    """V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing:
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing`
        """
        model = V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing(self):
        """Test V0041OpenapiSlurmdbdConfigRespQosInnerLimitsMaxActiveJobsAccruing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
