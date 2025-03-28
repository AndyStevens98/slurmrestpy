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

from slurmrestpy.models.v0042_cluster_rec_controller import V0042ClusterRecController


class TestV0042ClusterRecController(unittest.TestCase):
    """V0042ClusterRecController unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042ClusterRecController:
        """Test V0042ClusterRecController
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042ClusterRecController`
        """
        model = V0042ClusterRecController()
        if include_optional:
            return V0042ClusterRecController(
                host = '',
                port = 56
            )
        else:
            return V0042ClusterRecController(
        )
        """

    def testV0042ClusterRecController(self):
        """Test V0042ClusterRecController"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
