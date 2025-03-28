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

from slurmrestpy.models.v0041_openapi_reservation_resp_reservations_inner_core_specializations_inner import (
    V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner,
)


class TestV0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner(
    unittest.TestCase
):
    """V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner:
        """Test V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner`
        """
        model = V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner()
        if include_optional:
            return V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner(
                node = '',
                core = ''
            )
        else:
            return V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner(
        )
        """

    def testV0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner(self):
        """Test V0041OpenapiReservationRespReservationsInnerCoreSpecializationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
