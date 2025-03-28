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

from slurmrestpy.models.v0040_cluster_rec_associations import (
    V0040ClusterRecAssociations,
)


class TestV0040ClusterRecAssociations(unittest.TestCase):
    """V0040ClusterRecAssociations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040ClusterRecAssociations:
        """Test V0040ClusterRecAssociations
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040ClusterRecAssociations`
        """
        model = V0040ClusterRecAssociations()
        if include_optional:
            return V0040ClusterRecAssociations(
                root = slurmrestpy.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                    account = '',
                    cluster = '',
                    partition = '',
                    user = '',
                    id = 56, )
            )
        else:
            return V0040ClusterRecAssociations(
        )
        """

    def testV0040ClusterRecAssociations(self):
        """Test V0040ClusterRecAssociations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
