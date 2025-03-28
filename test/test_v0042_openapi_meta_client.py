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

from slurmrestpy.models.v0042_openapi_meta_client import V0042OpenapiMetaClient


class TestV0042OpenapiMetaClient(unittest.TestCase):
    """V0042OpenapiMetaClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiMetaClient:
        """Test V0042OpenapiMetaClient
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042OpenapiMetaClient`
        """
        model = V0042OpenapiMetaClient()
        if include_optional:
            return V0042OpenapiMetaClient(
                source = '',
                user = '',
                group = ''
            )
        else:
            return V0042OpenapiMetaClient(
        )
        """

    def testV0042OpenapiMetaClient(self):
        """Test V0042OpenapiMetaClient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
