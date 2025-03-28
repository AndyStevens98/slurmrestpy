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

from slurmrestpy.models.v0040_qos_limits_max_jobs_active_jobs import (
    V0040QosLimitsMaxJobsActiveJobs,
)


class TestV0040QosLimitsMaxJobsActiveJobs(unittest.TestCase):
    """V0040QosLimitsMaxJobsActiveJobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040QosLimitsMaxJobsActiveJobs:
        """Test V0040QosLimitsMaxJobsActiveJobs
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040QosLimitsMaxJobsActiveJobs`
        """
        model = V0040QosLimitsMaxJobsActiveJobs()
        if include_optional:
            return V0040QosLimitsMaxJobsActiveJobs(
                per = slurmrestpy.models.v0_0_40_qos_limits_max_jobs_active_jobs_per.v0_0_40_qos_limits_max_jobs_active_jobs_per(
                    account = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    user = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ), )
            )
        else:
            return V0040QosLimitsMaxJobsActiveJobs(
        )
        """

    def testV0040QosLimitsMaxJobsActiveJobs(self):
        """Test V0040QosLimitsMaxJobsActiveJobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
