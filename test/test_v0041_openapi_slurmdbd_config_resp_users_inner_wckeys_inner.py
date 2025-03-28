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

from slurmrestpy.models.v0041_openapi_slurmdbd_config_resp_users_inner_wckeys_inner import (
    V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner,
)


class TestV0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner(unittest.TestCase):
    """V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner:
        """Test V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner`
        """
        model = V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner()
        if include_optional:
            return V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner(
                accounting = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner(
                        allocated = slurmrestpy.models.v0_0_40_accounting_allocated.v0_0_40_accounting_allocated(
                            seconds = 56, ),
                        id = 56,
                        start = 56,
                        tres = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_tres.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner_accounting_inner_TRES(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, ), )
                    ],
                cluster = '',
                id = 56,
                name = '',
                user = '',
                flags = [
                    'DELETED'
                    ]
            )
        else:
            return V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner(
                cluster = '',
                name = '',
                user = '',
        )
        """

    def testV0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner(self):
        """Test V0041OpenapiSlurmdbdConfigRespUsersInnerWckeysInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
