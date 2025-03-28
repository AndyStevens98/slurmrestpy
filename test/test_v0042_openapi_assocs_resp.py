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

from slurmrestpy.models.v0042_openapi_assocs_resp import V0042OpenapiAssocsResp


class TestV0042OpenapiAssocsResp(unittest.TestCase):
    """V0042OpenapiAssocsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiAssocsResp:
        """Test V0042OpenapiAssocsResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042OpenapiAssocsResp`
        """
        model = V0042OpenapiAssocsResp()
        if include_optional:
            return V0042OpenapiAssocsResp(
                associations = [
                    slurmrestpy.models.v0/0/42_assoc.v0.0.42_assoc(
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
                        account = '',
                        cluster = '',
                        comment = '',
                        default = slurmrestpy.models.v0_0_42_assoc_default.v0_0_42_assoc_default(
                            qos = '', ),
                        flags = [
                            'DELETED'
                            ],
                        max = slurmrestpy.models.v0_0_42_assoc_max.v0_0_42_assoc_max(
                            jobs = slurmrestpy.models.v0_0_42_assoc_max_jobs.v0_0_42_assoc_max_jobs(
                                per = slurmrestpy.models.v0_0_42_assoc_max_jobs_per.v0_0_42_assoc_max_jobs_per(
                                    count = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                        set = True,
                                        infinite = True,
                                        number = 56, ),
                                    accruing = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                        set = True,
                                        infinite = True,
                                        number = 56, ),
                                    submitted = ,
                                    wall_clock = , ),
                                active = ,
                                accruing = ,
                                total = , ),
                            tres = slurmrestpy.models.v0_0_42_assoc_max_tres.v0_0_42_assoc_max_tres(
                                group = slurmrestpy.models.v0_0_42_assoc_max_tres_group.v0_0_42_assoc_max_tres_group(
                                    minutes = [
                                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                                            type = '',
                                            name = '',
                                            id = 56, )
                                        ], ),
                                minutes = slurmrestpy.models.v0_0_42_assoc_max_tres_minutes.v0_0_42_assoc_max_tres_minutes(), ),
                            per = slurmrestpy.models.v0_0_42_assoc_max_per.v0_0_42_assoc_max_per(
                                account = slurmrestpy.models.v0_0_42_assoc_max_per_account.v0_0_42_assoc_max_per_account(), ), ),
                        id = 56,
                        is_default = True,
                        lineage = '',
                        min = slurmrestpy.models.v0_0_42_assoc_min.v0_0_42_assoc_min(
                            priority_threshold = , ),
                        parent_account = '',
                        partition = '',
                        priority = ,
                        qos = [
                            ''
                            ],
                        shares_raw = 56,
                        user = '', )
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
            return V0042OpenapiAssocsResp(
                associations = [
                    slurmrestpy.models.v0/0/42_assoc.v0.0.42_assoc(
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
                        account = '',
                        cluster = '',
                        comment = '',
                        default = slurmrestpy.models.v0_0_42_assoc_default.v0_0_42_assoc_default(
                            qos = '', ),
                        flags = [
                            'DELETED'
                            ],
                        max = slurmrestpy.models.v0_0_42_assoc_max.v0_0_42_assoc_max(
                            jobs = slurmrestpy.models.v0_0_42_assoc_max_jobs.v0_0_42_assoc_max_jobs(
                                per = slurmrestpy.models.v0_0_42_assoc_max_jobs_per.v0_0_42_assoc_max_jobs_per(
                                    count = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                        set = True,
                                        infinite = True,
                                        number = 56, ),
                                    accruing = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                                        set = True,
                                        infinite = True,
                                        number = 56, ),
                                    submitted = ,
                                    wall_clock = , ),
                                active = ,
                                accruing = ,
                                total = , ),
                            tres = slurmrestpy.models.v0_0_42_assoc_max_tres.v0_0_42_assoc_max_tres(
                                group = slurmrestpy.models.v0_0_42_assoc_max_tres_group.v0_0_42_assoc_max_tres_group(
                                    minutes = [
                                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                                            type = '',
                                            name = '',
                                            id = 56, )
                                        ], ),
                                minutes = slurmrestpy.models.v0_0_42_assoc_max_tres_minutes.v0_0_42_assoc_max_tres_minutes(), ),
                            per = slurmrestpy.models.v0_0_42_assoc_max_per.v0_0_42_assoc_max_per(
                                account = slurmrestpy.models.v0_0_42_assoc_max_per_account.v0_0_42_assoc_max_per_account(), ), ),
                        id = 56,
                        is_default = True,
                        lineage = '',
                        min = slurmrestpy.models.v0_0_42_assoc_min.v0_0_42_assoc_min(
                            priority_threshold = , ),
                        parent_account = '',
                        partition = '',
                        priority = ,
                        qos = [
                            ''
                            ],
                        shares_raw = 56,
                        user = '', )
                    ],
        )
        """

    def testV0042OpenapiAssocsResp(self):
        """Test V0042OpenapiAssocsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
