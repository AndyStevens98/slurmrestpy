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

from slurmrestpy.models.v0040_step_nodes import V0040StepNodes


class TestV0040StepNodes(unittest.TestCase):
    """V0040StepNodes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040StepNodes:
        """Test V0040StepNodes
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040StepNodes`
        """
        model = V0040StepNodes()
        if include_optional:
            return V0040StepNodes(
                count = 56,
                range = '',
                list = [
                    ''
                    ]
            )
        else:
            return V0040StepNodes(
        )
        """

    def testV0040StepNodes(self):
        """Test V0040StepNodes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
