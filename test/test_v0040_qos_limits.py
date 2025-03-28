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

from slurmrestpy.models.v0040_qos_limits import V0040QosLimits


class TestV0040QosLimits(unittest.TestCase):
    """V0040QosLimits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040QosLimits:
        """Test V0040QosLimits
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040QosLimits`
        """
        model = V0040QosLimits()
        if include_optional:
            return V0040QosLimits(
                grace_time = 56,
                max = slurmrestpy.models.v0_0_40_qos_limits_max.v0_0_40_qos_limits_max(
                    active_jobs = slurmrestpy.models.v0_0_40_qos_limits_max_active_jobs.v0_0_40_qos_limits_max_active_jobs(
                        accruing = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        count = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ), ),
                    tres = slurmrestpy.models.v0_0_40_qos_limits_max_tres.v0_0_40_qos_limits_max_tres(
                        total = [
                            slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                                type = '',
                                name = '',
                                id = 56, )
                            ],
                        minutes = slurmrestpy.models.v0_0_40_qos_limits_max_tres_minutes.v0_0_40_qos_limits_max_tres_minutes(
                            per = slurmrestpy.models.v0_0_40_qos_limits_max_tres_minutes_per.v0_0_40_qos_limits_max_tres_minutes_per(
                                qos = [
                                    slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                                        type = '',
                                        name = '',
                                        id = 56, )
                                    ],
                                job = ,
                                account = ,
                                user = , ), ),
                        per = slurmrestpy.models.v0_0_40_qos_limits_max_tres_per.v0_0_40_qos_limits_max_tres_per(
                            account = ,
                            job = ,
                            node = ,
                            user = , ), ),
                    wall_clock = slurmrestpy.models.v0_0_40_qos_limits_max_wall_clock.v0_0_40_qos_limits_max_wall_clock(),
                    jobs = slurmrestpy.models.v0_0_40_qos_limits_max_jobs.v0_0_40_qos_limits_max_jobs(),
                    accruing = slurmrestpy.models.v0_0_40_qos_limits_max_jobs_active_jobs.v0_0_40_qos_limits_max_jobs_active_jobs(), ),
                factor = slurmrestpy.models.v0/0/40_float64_no_val.v0.0.40_float64_no_val(
                    set = True,
                    infinite = True,
                    number = 1.337, ),
                min = slurmrestpy.models.v0_0_40_qos_limits_min.v0_0_40_qos_limits_min(
                    priority_threshold = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    tres = slurmrestpy.models.v0_0_40_qos_limits_min_tres.v0_0_40_qos_limits_min_tres(
                        per = slurmrestpy.models.v0_0_40_qos_limits_min_tres_per.v0_0_40_qos_limits_min_tres_per(
                            job = [
                                slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                                    type = '',
                                    name = '',
                                    id = 56,
                                    count = 56, )
                                ], ), ), )
            )
        else:
            return V0040QosLimits(
        )
        """

    def testV0040QosLimits(self):
        """Test V0040QosLimits"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
