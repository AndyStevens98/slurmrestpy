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

from slurmrestpy.models.v0041_openapi_shares_resp_shares_shares_inner_tres_usage_inner import (
    V0041OpenapiSharesRespSharesSharesInnerTresUsageInner,
)


class TestV0041OpenapiSharesRespSharesSharesInnerTresUsageInner(unittest.TestCase):
    """V0041OpenapiSharesRespSharesSharesInnerTresUsageInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSharesRespSharesSharesInnerTresUsageInner:
        """Test V0041OpenapiSharesRespSharesSharesInnerTresUsageInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSharesRespSharesSharesInnerTresUsageInner`
        """
        model = V0041OpenapiSharesRespSharesSharesInnerTresUsageInner()
        if include_optional:
            return V0041OpenapiSharesRespSharesSharesInnerTresUsageInner(
                name = '',
                value = 1.337
            )
        else:
            return V0041OpenapiSharesRespSharesSharesInnerTresUsageInner(
        )
        """

    def testV0041OpenapiSharesRespSharesSharesInnerTresUsageInner(self):
        """Test V0041OpenapiSharesRespSharesSharesInnerTresUsageInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
