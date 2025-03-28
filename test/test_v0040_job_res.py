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

from slurmrestpy.models.v0040_job_res import V0040JobRes


class TestV0040JobRes(unittest.TestCase):
    """V0040JobRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040JobRes:
        """Test V0040JobRes
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040JobRes`
        """
        model = V0040JobRes()
        if include_optional:
            return V0040JobRes(
                nodes = '',
                allocated_cores = 56,
                allocated_cpus = 56,
                allocated_hosts = 56,
                allocated_nodes = [
                    null
                    ]
            )
        else:
            return V0040JobRes(
        )
        """

    def testV0040JobRes(self):
        """Test V0040JobRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
