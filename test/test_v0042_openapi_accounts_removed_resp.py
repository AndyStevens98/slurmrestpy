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

from slurmrestpy.models.v0042_openapi_accounts_removed_resp import (
    V0042OpenapiAccountsRemovedResp,
)


class TestV0042OpenapiAccountsRemovedResp(unittest.TestCase):
    """V0042OpenapiAccountsRemovedResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiAccountsRemovedResp:
        """Test V0042OpenapiAccountsRemovedResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042OpenapiAccountsRemovedResp`
        """
        model = V0042OpenapiAccountsRemovedResp()
        if include_optional:
            return V0042OpenapiAccountsRemovedResp(
                removed_accounts = [
                    ''
                    ],
                meta = slurmrestpy.models.v0/0/42_openapi_meta.v0.0.42_openapi_meta(
                    plugin = slurmrestpy.models.v0_0_42_openapi_meta_plugin.v0_0_42_openapi_meta_plugin(
                        type = '',
                        name = '',
                        data_parser = '',
                        accounting_storage = '', ),
                    client = slurmrestpy.models.v0_0_42_openapi_meta_client.v0_0_42_openapi_meta_client(
                        source = '',
                        user = '',
                        group = '', ),
                    command = [
                        ''
                        ],
                    slurm = slurmrestpy.models.v0_0_42_openapi_meta_slurm.v0_0_42_openapi_meta_slurm(
                        version = slurmrestpy.models.v0_0_42_openapi_meta_slurm_version.v0_0_42_openapi_meta_slurm_version(
                            major = '',
                            micro = '',
                            minor = '', ),
                        release = '',
                        cluster = '', ), ),
                errors = [
                    slurmrestpy.models.v0/0/42_openapi_error.v0.0.42_openapi_error(
                        description = '',
                        error_number = 56,
                        error = '',
                        source = '', )
                    ],
                warnings = [
                    slurmrestpy.models.v0/0/42_openapi_warning.v0.0.42_openapi_warning(
                        description = '',
                        source = '', )
                    ]
            )
        else:
            return V0042OpenapiAccountsRemovedResp(
                removed_accounts = [
                    ''
                    ],
        )
        """

    def testV0042OpenapiAccountsRemovedResp(self):
        """Test V0042OpenapiAccountsRemovedResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
