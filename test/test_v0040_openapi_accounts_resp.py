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

from slurmrestpy.models.v0040_openapi_accounts_resp import V0040OpenapiAccountsResp


class TestV0040OpenapiAccountsResp(unittest.TestCase):
    """V0040OpenapiAccountsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040OpenapiAccountsResp:
        """Test V0040OpenapiAccountsResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040OpenapiAccountsResp`
        """
        model = V0040OpenapiAccountsResp()
        if include_optional:
            return V0040OpenapiAccountsResp(
                accounts = [
                    slurmrestpy.models.v0/0/40_account.v0.0.40_account(
                        associations = [
                            slurmrestpy.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                                account = '',
                                cluster = '',
                                partition = '',
                                user = '',
                                id = 56, )
                            ],
                        coordinators = [
                            slurmrestpy.models.v0/0/40_coord.v0.0.40_coord(
                                name = '',
                                direct = True, )
                            ],
                        description = '',
                        name = '',
                        organization = '',
                        flags = [
                            'DELETED'
                            ], )
                    ],
                meta = slurmrestpy.models.v0/0/40_openapi_meta.v0.0.40_openapi_meta(
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
                    slurmrestpy.models.v0/0/40_openapi_error.v0.0.40_openapi_error(
                        description = '',
                        error_number = 56,
                        error = '',
                        source = '', )
                    ],
                warnings = [
                    slurmrestpy.models.v0/0/40_openapi_warning.v0.0.40_openapi_warning(
                        description = '',
                        source = '', )
                    ]
            )
        else:
            return V0040OpenapiAccountsResp(
                accounts = [
                    slurmrestpy.models.v0/0/40_account.v0.0.40_account(
                        associations = [
                            slurmrestpy.models.v0/0/40_assoc_short.v0.0.40_assoc_short(
                                account = '',
                                cluster = '',
                                partition = '',
                                user = '',
                                id = 56, )
                            ],
                        coordinators = [
                            slurmrestpy.models.v0/0/40_coord.v0.0.40_coord(
                                name = '',
                                direct = True, )
                            ],
                        description = '',
                        name = '',
                        organization = '',
                        flags = [
                            'DELETED'
                            ], )
                    ],
        )
        """

    def testV0040OpenapiAccountsResp(self):
        """Test V0040OpenapiAccountsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
