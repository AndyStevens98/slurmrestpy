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

from slurmrestpy.models.v0041_openapi_job_info_resp_jobs_inner_end_time import (
    V0041OpenapiJobInfoRespJobsInnerEndTime,
)


class TestV0041OpenapiJobInfoRespJobsInnerEndTime(unittest.TestCase):
    """V0041OpenapiJobInfoRespJobsInnerEndTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiJobInfoRespJobsInnerEndTime:
        """Test V0041OpenapiJobInfoRespJobsInnerEndTime
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiJobInfoRespJobsInnerEndTime`
        """
        model = V0041OpenapiJobInfoRespJobsInnerEndTime()
        if include_optional:
            return V0041OpenapiJobInfoRespJobsInnerEndTime(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiJobInfoRespJobsInnerEndTime(
        )
        """

    def testV0041OpenapiJobInfoRespJobsInnerEndTime(self):
        """Test V0041OpenapiJobInfoRespJobsInnerEndTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
