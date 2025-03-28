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

from slurmrestpy.models.v0040_step import V0040Step


class TestV0040Step(unittest.TestCase):
    """V0040Step unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0040Step:
        """Test V0040Step
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0040Step`
        """
        model = V0040Step()
        if include_optional:
            return V0040Step(
                time = slurmrestpy.models.v0_0_40_step_time.v0_0_40_step_time(
                    elapsed = 56,
                    end = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    start = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    suspended = 56,
                    system = slurmrestpy.models.v0_0_42_step_time_system.v0_0_42_step_time_system(
                        seconds = 56,
                        microseconds = 56, ),
                    total = slurmrestpy.models.v0_0_42_step_time_total.v0_0_42_step_time_total(
                        seconds = 56,
                        microseconds = 56, ),
                    user = slurmrestpy.models.v0_0_42_step_time_user.v0_0_42_step_time_user(
                        seconds = 56,
                        microseconds = 56, ), ),
                exit_code = slurmrestpy.models.v0/0/40_process_exit_code_verbose.v0.0.40_process_exit_code_verbose(
                    status = [
                        'INVALID'
                        ],
                    return_code = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    signal = slurmrestpy.models.v0_0_40_process_exit_code_verbose_signal.v0_0_40_process_exit_code_verbose_signal(
                        id = slurmrestpy.models.v0/0/40_uint16_no_val.v0.0.40_uint16_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        name = '', ), ),
                nodes = slurmrestpy.models.v0_0_40_step_nodes.v0_0_40_step_nodes(
                    count = 56,
                    range = '',
                    list = [
                        ''
                        ], ),
                tasks = slurmrestpy.models.v0_0_42_step_tasks.v0_0_42_step_tasks(
                    count = 56, ),
                pid = '',
                cpu = slurmrestpy.models.v0_0_40_step_cpu.v0_0_40_step_CPU(
                    requested_frequency = slurmrestpy.models.v0_0_40_step_cpu_requested_frequency.v0_0_40_step_CPU_requested_frequency(
                        min = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        max = slurmrestpy.models.v0/0/40_uint32_no_val.v0.0.40_uint32_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ), ),
                    governor = '', ),
                kill_request_user = '',
                state = [
                    'PENDING'
                    ],
                statistics = slurmrestpy.models.v0_0_40_step_statistics.v0_0_40_step_statistics(
                    cpu = slurmrestpy.models.v0_0_42_step_statistics_cpu.v0_0_42_step_statistics_CPU(
                        actual_frequency = 56, ),
                    energy = slurmrestpy.models.v0_0_40_step_statistics_energy.v0_0_40_step_statistics_energy(
                        consumed = slurmrestpy.models.v0/0/40_uint64_no_val.v0.0.40_uint64_no_val(
                            set = True,
                            infinite = True,
                            number = 56, ), ), ),
                step = slurmrestpy.models.v0_0_40_step_step.v0_0_40_step_step(
                    id = '',
                    name = '', ),
                task = slurmrestpy.models.v0_0_42_step_task.v0_0_42_step_task(
                    distribution = '', ),
                tres = slurmrestpy.models.v0_0_40_step_tres.v0_0_40_step_tres(
                    requested = slurmrestpy.models.v0_0_40_step_tres_requested.v0_0_40_step_tres_requested(
                        max = [
                            slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                                type = '',
                                name = '',
                                id = 56,
                                count = 56, )
                            ],
                        min = [
                            slurmrestpy.models.v0/0/40_tres.v0.0.40_tres(
                                type = '',
                                name = '',
                                id = 56,
                                count = 56, )
                            ],
                        average = [

                            ],
                        total = [

                            ], ),
                    consumed = slurmrestpy.models.v0_0_40_step_tres_consumed.v0_0_40_step_tres_consumed(),
                    allocated = , )
            )
        else:
            return V0040Step(
        )
        """

    def testV0040Step(self):
        """Test V0040Step"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
