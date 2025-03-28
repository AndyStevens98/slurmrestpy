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

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_associations_inner_max_jobs_accruing import (
    V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing,
)


class TestV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing(
    unittest.TestCase
):
    """V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing:
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing`
        """
        model = V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing(
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing(self):
        """Test V0041OpenapiSlurmdbdConfigRespAssociationsInnerMaxJobsAccruing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
