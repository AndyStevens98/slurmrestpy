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

from slurmrestpy.models.v0041_openapi_users_resp import V0041OpenapiUsersResp


class TestV0041OpenapiUsersResp(unittest.TestCase):
    """V0041OpenapiUsersResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiUsersResp:
        """Test V0041OpenapiUsersResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiUsersResp`
        """
        model = V0041OpenapiUsersResp()
        if include_optional:
            return V0041OpenapiUsersResp(
                users = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner.v0_0_41_openapi_slurmdbd_config_resp_users_inner(
                        administrator_level = [
                            'Not Set'
                            ],
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
                        default = slurmrestpy.models.v0_0_40_user_default.v0_0_40_user_default(
                            account = '',
                            wckey = '', ),
                        flags = [
                            'NONE'
                            ],
                        name = '',
                        old_name = '',
                        wckeys = [
                            slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner(
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
                                user = '', )
                            ], )
                    ],
                meta = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_meta.v0_0_41_openapi_slurmdbd_jobs_resp_meta(
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
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_errors_inner.v0_0_41_openapi_slurmdbd_jobs_resp_errors_inner(
                        description = '',
                        error_number = 56,
                        error = '',
                        source = '', )
                    ],
                warnings = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_warnings_inner.v0_0_41_openapi_slurmdbd_jobs_resp_warnings_inner(
                        description = '',
                        source = '', )
                    ]
            )
        else:
            return V0041OpenapiUsersResp(
                users = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner.v0_0_41_openapi_slurmdbd_config_resp_users_inner(
                        administrator_level = [
                            'Not Set'
                            ],
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
                        default = slurmrestpy.models.v0_0_40_user_default.v0_0_40_user_default(
                            account = '',
                            wckey = '', ),
                        flags = [
                            'NONE'
                            ],
                        name = '',
                        old_name = '',
                        wckeys = [
                            slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner.v0_0_41_openapi_slurmdbd_config_resp_users_inner_wckeys_inner(
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
                                user = '', )
                            ], )
                    ],
        )
        """

    def testV0041OpenapiUsersResp(self):
        """Test V0041OpenapiUsersResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
