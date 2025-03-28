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

from slurmrestpy.models.v0042_job_state import V0042JobState


class TestV0042JobState(unittest.TestCase):
    """V0042JobState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobState:
        """Test V0042JobState
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042JobState`
        """
        model = V0042JobState()
        if include_optional:
            return V0042JobState(
                current = [
                    'PENDING'
                    ],
                reason = ''
            )
        else:
            return V0042JobState(
        )
        """

    def testV0042JobState(self):
        """Test V0042JobState"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
