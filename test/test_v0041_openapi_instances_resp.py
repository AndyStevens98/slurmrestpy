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

from slurmrestpy.models.v0041_openapi_instances_resp import V0041OpenapiInstancesResp


class TestV0041OpenapiInstancesResp(unittest.TestCase):
    """V0041OpenapiInstancesResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiInstancesResp:
        """Test V0041OpenapiInstancesResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiInstancesResp`
        """
        model = V0041OpenapiInstancesResp()
        if include_optional:
            return V0041OpenapiInstancesResp(
                instances = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_instances_inner.v0_0_41_openapi_slurmdbd_config_resp_instances_inner(
                        cluster = '',
                        extra = '',
                        instance_id = '',
                        instance_type = '',
                        node_name = '',
                        time = slurmrestpy.models.v0_0_42_instance_time.v0_0_42_instance_time(
                            time_end = 56,
                            time_start = 56, ), )
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
            return V0041OpenapiInstancesResp(
                instances = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_instances_inner.v0_0_41_openapi_slurmdbd_config_resp_instances_inner(
                        cluster = '',
                        extra = '',
                        instance_id = '',
                        instance_type = '',
                        node_name = '',
                        time = slurmrestpy.models.v0_0_42_instance_time.v0_0_42_instance_time(
                            time_end = 56,
                            time_start = 56, ), )
                    ],
        )
        """

    def testV0041OpenapiInstancesResp(self):
        """Test V0041OpenapiInstancesResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
