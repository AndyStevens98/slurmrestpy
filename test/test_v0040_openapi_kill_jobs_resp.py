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

from slurmrestpy.models.v0040_openapi_kill_jobs_resp import V0040OpenapiKillJobsResp


class TestV0040OpenapiKillJobsResp(unittest.TestCase):
    """V0040OpenapiKillJobsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiKillJobsResp:
        """Test V0040OpenapiKillJobsResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040OpenapiKillJobsResp`
        """
        model = V0040OpenapiKillJobsResp()
        if include_optional:
            return V0040OpenapiKillJobsResp(
                status = [
                    slurmrestpy.models.v0/0/40_kill_jobs_resp_job.v0.0.40_kill_jobs_resp_job(
                        error = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_error.v0_0_42_kill_jobs_resp_job_error(
                            string = '',
                            code = 56,
                            message = '', ),
                        step_id = '',
                        job_id = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        federation = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_federation.v0_0_42_kill_jobs_resp_job_federation(
                            sibling = '', ), )
                    ],
                meta = slurmrestpy.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
                    plugin = slurmrestpy.models.v0_0_42_openapi_meta_plugin.v0_0_42_openapi_meta_plugin(
                        type = '',
                        name = '',
                        data_parser = '',
                        accounting_storage = '', ),
                    client = slurmrestpy.models.v0_0_42_openapi_meta_client.v0_0_42_openapi_meta_client(
                        source = '',
                        user = '',
                        group = '', ),
                    command = [
                        ''
                        ],
                    slurm = slurmrestpy.models.v0_0_42_openapi_meta_slurm.v0_0_42_openapi_meta_slurm(
                        version = slurmrestpy.models.v0_0_42_openapi_meta_slurm_version.v0_0_42_openapi_meta_slurm_version(
                            major = '',
                            micro = '',
                            minor = '', ),
                        release = '',
                        cluster = '', ), ),
                errors = [
                    slurmrestpy.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '',
                        error_number = 56,
                        error = '',
                        source = '', )
                    ],
                warnings = [
                    slurmrestpy.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '',
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiKillJobsResp(
                status = [
                    slurmrestpy.models.v0/0/40_kill_jobs_resp_job.v0.0.40_kill_jobs_resp_job(
                        error = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_error.v0_0_42_kill_jobs_resp_job_error(
                            string = '',
                            code = 56,
                            message = '', ),
                        step_id = '',
                        job_id = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        federation = slurmrestpy.models.v0_0_42_kill_jobs_resp_job_federation.v0_0_42_kill_jobs_resp_job_federation(
                            sibling = '', ), )
                    ],
        )
        """

    def testV0040OpenapiKillJobsResp(self):
        """Test V0040OpenapiKillJobsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
