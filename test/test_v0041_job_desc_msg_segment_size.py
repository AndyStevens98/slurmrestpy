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

from slurmrestpy.models.v0041_job_desc_msg_segment_size import (
    V0041JobDescMsgSegmentSize,
)


class TestV0041JobDescMsgSegmentSize(unittest.TestCase):
    """V0041JobDescMsgSegmentSize unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041JobDescMsgSegmentSize:
        """Test V0041JobDescMsgSegmentSize
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041JobDescMsgSegmentSize`
        """
        model = V0041JobDescMsgSegmentSize()
        if include_optional:
            return V0041JobDescMsgSegmentSize(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041JobDescMsgSegmentSize(
        )
        """

    def testV0041JobDescMsgSegmentSize(self):
        """Test V0041JobDescMsgSegmentSize"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
