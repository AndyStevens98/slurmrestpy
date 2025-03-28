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

from slurmrestpy.models.v0040_kill_jobs_msg import V0040KillJobsMsg


class TestV0040KillJobsMsg(unittest.TestCase):
    """V0040KillJobsMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040KillJobsMsg:
        """Test V0040KillJobsMsg
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040KillJobsMsg`
        """
        model = V0040KillJobsMsg()
        if include_optional:
            return V0040KillJobsMsg(
                account = '',
                flags = [
                    'BATCH_JOB'
                    ],
                job_name = '',
                jobs = [
                    ''
                    ],
                partition = '',
                qos = '',
                reservation = '',
                signal = '',
                job_state = [
                    'PENDING'
                    ],
                user_id = '',
                user_name = '',
                wckey = '',
                nodes = [
                    ''
                    ]
            )
        else:
            return V0040KillJobsMsg(
        )
        """

    def testV0040KillJobsMsg(self):
        """Test V0040KillJobsMsg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
