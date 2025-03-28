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

from slurmrestpy.models.v0041_openapi_kill_jobs_resp_status_inner import (
    V0041OpenapiKillJobsRespStatusInner,
)


class TestV0041OpenapiKillJobsRespStatusInner(unittest.TestCase):
    """V0041OpenapiKillJobsRespStatusInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiKillJobsRespStatusInner:
        """Test V0041OpenapiKillJobsRespStatusInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiKillJobsRespStatusInner`
        """
        model = V0041OpenapiKillJobsRespStatusInner()
        if include_optional:
            return V0041OpenapiKillJobsRespStatusInner(
                error = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_error.v0_0_42_kill_jobs_resp_job_error(
                    string = '',
                    code = 56,
                    message = '', ),
                step_id = '',
                job_id = slurmrestpy.models.v0_0_41_openapi_kill_jobs_resp_status_inner_job_id.v0_0_41_openapi_kill_jobs_resp_status_inner_job_id(
                    set = True,
                    infinite = True,
                    number = 56, ),
                federation = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_federation.v0_0_42_kill_jobs_resp_job_federation(
                    sibling = '', )
            )
        else:
            return V0041OpenapiKillJobsRespStatusInner(
                step_id = '',
                job_id = slurmrestpy.models.v0_0_41_openapi_kill_jobs_resp_status_inner_job_id.v0_0_41_openapi_kill_jobs_resp_status_inner_job_id(
                    set = True,
                    infinite = True,
                    number = 56, ),
        )
        """

    def testV0041OpenapiKillJobsRespStatusInner(self):
        """Test V0041OpenapiKillJobsRespStatusInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
