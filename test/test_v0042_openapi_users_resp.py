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

from slurmrestpy.models.v0042_openapi_users_resp import V0042OpenapiUsersResp


class TestV0042OpenapiUsersResp(unittest.TestCase):
    """V0042OpenapiUsersResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiUsersResp:
        """Test V0042OpenapiUsersResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042OpenapiUsersResp`
        """
        model = V0042OpenapiUsersResp()
        if include_optional:
            return V0042OpenapiUsersResp(
                users = [
                    slurmrestpy.models.v0/0/42_user.v0.0.42_user(
                        administrator_level = [
                            'Not Set'
                            ],
                        associations = [
                            slurmrestpy.models.v0/0/42_assoc_short.v0.0.42_assoc_short(
                                account = '',
                                cluster = '',
                                partition = '',
                                user = '',
                                id = 56, )
                            ],
                        coordinators = [
                            slurmrestpy.models.v0/0/42_coord.v0.0.42_coord(
                                name = '',
                                direct = True, )
                            ],
                        default = slurmrestpy.models.v0_0_42_user_default.v0_0_42_user_default(
                            account = '',
                            wckey = '', ),
                        flags = [
                            'NONE'
                            ],
                        name = '',
                        old_name = '',
                        wckeys = [
                            slurmrestpy.models.v0/0/42_wckey.v0.0.42_wckey(
                                accounting = [
                                    slurmrestpy.models.v0/0/42_accounting.v0.0.42_accounting(
                                        allocated = slurmrestpy.models.v0_0_42_accounting_allocated.v0_0_42_accounting_allocated(
                                            seconds = 56, ),
                                        id = 56,
                                        id_alt = 56,
                                        start = 56,
                                        tres = slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
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
                                    ], )
                            ], )
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
            return V0042OpenapiUsersResp(
                users = [
                    slurmrestpy.models.v0/0/42_user.v0.0.42_user(
                        administrator_level = [
                            'Not Set'
                            ],
                        associations = [
                            slurmrestpy.models.v0/0/42_assoc_short.v0.0.42_assoc_short(
                                account = '',
                                cluster = '',
                                partition = '',
                                user = '',
                                id = 56, )
                            ],
                        coordinators = [
                            slurmrestpy.models.v0/0/42_coord.v0.0.42_coord(
                                name = '',
                                direct = True, )
                            ],
                        default = slurmrestpy.models.v0_0_42_user_default.v0_0_42_user_default(
                            account = '',
                            wckey = '', ),
                        flags = [
                            'NONE'
                            ],
                        name = '',
                        old_name = '',
                        wckeys = [
                            slurmrestpy.models.v0/0/42_wckey.v0.0.42_wckey(
                                accounting = [
                                    slurmrestpy.models.v0/0/42_accounting.v0.0.42_accounting(
                                        allocated = slurmrestpy.models.v0_0_42_accounting_allocated.v0_0_42_accounting_allocated(
                                            seconds = 56, ),
                                        id = 56,
                                        id_alt = 56,
                                        start = 56,
                                        tres = slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
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
                                    ], )
                            ], )
                    ],
        )
        """

    def testV0042OpenapiUsersResp(self):
        """Test V0042OpenapiUsersResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
