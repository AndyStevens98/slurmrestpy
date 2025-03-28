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

from slurmrestpy.models.v0042_kill_jobs_resp_job import V0042KillJobsRespJob


class TestV0042KillJobsRespJob(unittest.TestCase):
    """V0042KillJobsRespJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042KillJobsRespJob:
        """Test V0042KillJobsRespJob
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042KillJobsRespJob`
        """
        model = V0042KillJobsRespJob()
        if include_optional:
            return V0042KillJobsRespJob(
                error = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_error.v0_0_42_kill_jobs_resp_job_error(
                    string = '',
                    code = 56,
                    message = '', ),
                step_id = '',
                job_id = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                federation = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_federation.v0_0_42_kill_jobs_resp_job_federation(
                    sibling = '', )
            )
        else:
            return V0042KillJobsRespJob(
                step_id = '',
                job_id = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
        )
        """

    def testV0042KillJobsRespJob(self):
        """Test V0042KillJobsRespJob"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
