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

from slurmrestpy.models.v0040_reservation_core_spec import V0040ReservationCoreSpec


class TestV0040ReservationCoreSpec(unittest.TestCase):
    """V0040ReservationCoreSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040ReservationCoreSpec:
        """Test V0040ReservationCoreSpec
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040ReservationCoreSpec`
        """
        model = V0040ReservationCoreSpec()
        if include_optional:
            return V0040ReservationCoreSpec(
                node = '',
                core = ''
            )
        else:
            return V0040ReservationCoreSpec(
        )
        """

    def testV0040ReservationCoreSpec(self):
        """Test V0040ReservationCoreSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
