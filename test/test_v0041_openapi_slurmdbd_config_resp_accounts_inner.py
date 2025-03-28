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

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_accounts_inner import (
    V0041OpenapiSlurmdbdConfigRespAccountsInner,
)


class TestV0041OpenapiSlurmdbdConfigRespAccountsInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespAccountsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSlurmdbdConfigRespAccountsInner:
        """Test V0041OpenapiSlurmdbdConfigRespAccountsInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespAccountsInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespAccountsInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespAccountsInner(
                associations = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_accounts_inner_associations_inner.v0_0_41_openapi_slurmdbd_config_resp_accounts_inner_associations_inner(
                        account = '',
                        cluster = '',
                        partition = '',
                        user = '',
                        id = 56, )
                    ],
                coordinators = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_accounts_inner_coordinators_inner.v0_0_41_openapi_slurmdbd_config_resp_accounts_inner_coordinators_inner(
                        name = '',
                        direct = True, )
                    ],
                description = '',
                name = '',
                organization = '',
                flags = [
                    'DELETED'
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespAccountsInner(
                description = '',
                name = '',
                organization = '',
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespAccountsInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespAccountsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
