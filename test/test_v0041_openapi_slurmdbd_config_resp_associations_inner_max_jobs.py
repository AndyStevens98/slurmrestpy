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

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs import (
    V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs,
)


class TestV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs(
                per = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per(
                    count = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_count(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    accruing = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_active_jobs_accruing(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    submitted = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_submitted.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_per_submitted(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    wall_clock = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job.v0_0_41_openapi_slurmdbd_config_resp_qos_inner_limits_max_wall_clock_per_job(
                        set = True,
                        infinite = True,
                        number = 56, ), ),
                active = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_active.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_active(
                    set = True,
                    infinite = True,
                    number = 56, ),
                accruing = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_accruing.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_accruing(
                    set = True,
                    infinite = True,
                    number = 56, ),
                total = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_total.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_max_jobs_total(
                    set = True,
                    infinite = True,
                    number = 56, )
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
