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

from slurmrestpy.models.v0041_openapi_diag_resp_statistics_rpcs_by_message_type_inner import (
    V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner,
)


class TestV0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner(unittest.TestCase):
    """V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner:
        """Test V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner`
        """
        model = V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner()
        if include_optional:
            return V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner(
                type_id = 56,
                message_type = '',
                count = 56,
                queued = 56,
                dropped = 56,
                cycle_last = 56,
                cycle_max = 56,
                total_time = 56,
                average_time = slurmrestpy.models.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time(
                    set = True,
                    infinite = True,
                    number = 56, )
            )
        else:
            return V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner(
                type_id = 56,
                message_type = '',
                count = 56,
                queued = 56,
                dropped = 56,
                cycle_last = 56,
                cycle_max = 56,
                total_time = 56,
                average_time = slurmrestpy.models.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time.v0_0_41_openapi_diag_resp_statistics_rpcs_by_message_type_inner_average_time(
                    set = True,
                    infinite = True,
                    number = 56, ),
        )
        """

    def testV0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner(self):
        """Test V0041OpenapiDiagRespStatisticsRpcsByMessageTypeInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
