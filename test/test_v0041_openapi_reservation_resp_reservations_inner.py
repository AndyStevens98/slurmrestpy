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

from slurmrestpy.models.v0041_openapi_reservation_resp_reservations_inner import (
    V0041OpenapiReservationRespReservationsInner,
)


class TestV0041OpenapiReservationRespReservationsInner(unittest.TestCase):
    """V0041OpenapiReservationRespReservationsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiReservationRespReservationsInner:
        """Test V0041OpenapiReservationRespReservationsInner
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiReservationRespReservationsInner`
        """
        model = V0041OpenapiReservationRespReservationsInner()
        if include_optional:
            return V0041OpenapiReservationRespReservationsInner(
                accounts = '',
                burst_buffer = '',
                core_count = 56,
                core_specializations = [
                    slurmrestpy.models.v0_0_41_openapi_reservation_resp_reservations_inner_core_specializations_inner.v0_0_41_openapi_reservation_resp_reservations_inner_core_specializations_inner(
                        node = '',
                        core = '', )
                    ],
                end_time = slurmrestpy.models.v0_0_41_openapi_reservation_resp_reservations_inner_end_time.v0_0_41_openapi_reservation_resp_reservations_inner_end_time(
                    set = True,
                    infinite = True,
                    number = 56, ),
                features = '',
                flags = [
                    'MAINT'
                    ],
                groups = '',
                licenses = '',
                max_start_delay = 56,
                name = '',
                node_count = 56,
                node_list = '',
                partition = '',
                purge_completed = slurmrestpy.models.v0_0_41_openapi_reservation_resp_reservations_inner_purge_completed.v0_0_41_openapi_reservation_resp_reservations_inner_purge_completed(
                    time = slurmrestpy.models.v0_0_41_openapi_reservation_resp_reservations_inner_purge_completed_time.v0_0_41_openapi_reservation_resp_reservations_inner_purge_completed_time(
                        set = True,
                        infinite = True,
                        number = 56, ), ),
                start_time = slurmrestpy.models.v0_0_41_openapi_reservation_resp_reservations_inner_start_time.v0_0_41_openapi_reservation_resp_reservations_inner_start_time(
                    set = True,
                    infinite = True,
                    number = 56, ),
                watts = slurmrestpy.models.v0_0_41_openapi_reservation_resp_reservations_inner_watts.v0_0_41_openapi_reservation_resp_reservations_inner_watts(
                    set = True,
                    infinite = True,
                    number = 56, ),
                tres = '',
                users = ''
            )
        else:
            return V0041OpenapiReservationRespReservationsInner(
        )
        """

    def testV0041OpenapiReservationRespReservationsInner(self):
        """Test V0041OpenapiReservationRespReservationsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
