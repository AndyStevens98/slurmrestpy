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

from slurmrestpy.models.v0041_openapi_slurmdbd_jobs_resp import (
    V0041OpenapiSlurmdbdJobsResp,
)


class TestV0041OpenapiSlurmdbdJobsResp(unittest.TestCase):
    """V0041OpenapiSlurmdbdJobsResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0041OpenapiSlurmdbdJobsResp:
        """Test V0041OpenapiSlurmdbdJobsResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiSlurmdbdJobsResp`
        """
        model = V0041OpenapiSlurmdbdJobsResp()
        if include_optional:
            return V0041OpenapiSlurmdbdJobsResp(
                jobs = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner(
                        account = '',
                        comment = slurmrestpy.models.v0_0_42_job_comment.v0_0_42_job_comment(
                            administrator = '',
                            job = '',
                            system = '', ),
                        allocation_nodes = 56,
                        array = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array(
                            job_id = 56,
                            limits = slurmrestpy.models.v0_0_42_job_array_limits.v0_0_42_job_array_limits(
                                max = slurmrestpy.models.v0_0_42_job_array_limits_max.v0_0_42_job_array_limits_max(
                                    running = slurmrestpy.models.v0_0_42_job_array_limits_max_running.v0_0_42_job_array_limits_max_running(
                                        tasks = 56, ), ), ),
                            task_id = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            task = '', ),
                        association = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association(
                            account = '',
                            cluster = '',
                            partition = '',
                            user = '',
                            id = 56, ),
                        block = '',
                        cluster = '',
                        constraints = '',
                        container = '',
                        derived_exit_code = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code(
                            status = [
                                'INVALID'
                                ],
                            return_code = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_return_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_return_code(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            signal = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal(
                                id = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal_id(
                                    set = True,
                                    infinite = True,
                                    number = 56, ),
                                name = '', ), ),
                        time = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time(
                            elapsed = 56,
                            eligible = 56,
                            end = 56,
                            planned = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            start = 56,
                            submission = 56,
                            suspended = 56,
                            system = slurmrestpy.models.v0_0_42_job_time_system.v0_0_42_job_time_system(
                                seconds = 56,
                                microseconds = 56, ),
                            limit = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_limit.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_limit(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            total = slurmrestpy.models.v0_0_42_job_time_total.v0_0_42_job_time_total(
                                seconds = 56,
                                microseconds = 56, ),
                            user = slurmrestpy.models.v0_0_42_job_time_user.v0_0_42_job_time_user(
                                seconds = 56,
                                microseconds = 56, ), ),
                        exit_code = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code(),
                        extra = '',
                        failed_node = '',
                        flags = [
                            'NONE'
                            ],
                        group = '',
                        het = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het(
                            job_id = 56,
                            job_offset = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het_job_offset.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het_job_offset(
                                set = True,
                                infinite = True,
                                number = 56, ), ),
                        job_id = 56,
                        name = '',
                        licenses = '',
                        mcs = slurmrestpy.models.v0_0_42_job_mcs.v0_0_42_job_mcs(
                            label = '', ),
                        nodes = '',
                        partition = '',
                        hold = True,
                        priority = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_priority.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_priority(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        qos = '',
                        required = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required(
                            cpus = 56,
                            memory_per_cpu = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            memory_per_node = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_node.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_node(
                                set = True,
                                infinite = True,
                                number = 56, ), ),
                        kill_request_user = '',
                        reservation = slurmrestpy.models.v0_0_42_job_reservation.v0_0_42_job_reservation(
                            name = '', ),
                        script = '',
                        stdin_expanded = '',
                        stdout_expanded = '',
                        stderr_expanded = '',
                        stdout = '',
                        stderr = '',
                        stdin = '',
                        state = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_state.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_state(
                            current = [
                                'PENDING'
                                ],
                            reason = '', ),
                        steps = [
                            slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner(
                                nodes = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes(
                                    count = 56,
                                    range = '',
                                    list = [
                                        ''
                                        ], ),
                                tasks = slurmrestpy.models.v0_0_42_step_tasks.v0_0_42_step_tasks(
                                    count = 56, ),
                                pid = '',
                                cpu = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU(
                                    requested_frequency = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency(
                                        min = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency_min(
                                            set = True,
                                            infinite = True,
                                            number = 56, ), ),
                                    governor = '', ),
                                kill_request_user = '',
                                statistics = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics(
                                    energy = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy(
                                        consumed = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed(
                                            set = True,
                                            infinite = True,
                                            number = 56, ), ), ),
                                step = slurmrestpy.models.v0_0_42_step_step.v0_0_42_step_step(
                                    name = '', ),
                                task = slurmrestpy.models.v0_0_42_step_task.v0_0_42_step_task(
                                    distribution = '', ),
                                tres = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres(
                                    requested = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested(
                                        average = [
                                            slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                                type = '',
                                                name = '',
                                                count = 56, )
                                            ], ),
                                    allocated = [
                                        slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                            type = '',
                                            name = '',
                                            count = 56, )
                                        ], ), )
                            ],
                        submit_line = '',
                        tres = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_tres.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_tres(),
                        used_gres = '',
                        user = '',
                        wckey = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_wckey.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_wckey(
                            wckey = '',
                            flags = [
                                'ASSIGNED_DEFAULT'
                                ], ),
                        working_directory = '', )
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
            return V0041OpenapiSlurmdbdJobsResp(
                jobs = [
                    slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner(
                        account = '',
                        comment = slurmrestpy.models.v0_0_42_job_comment.v0_0_42_job_comment(
                            administrator = '',
                            job = '',
                            system = '', ),
                        allocation_nodes = 56,
                        array = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array(
                            job_id = 56,
                            limits = slurmrestpy.models.v0_0_42_job_array_limits.v0_0_42_job_array_limits(
                                max = slurmrestpy.models.v0_0_42_job_array_limits_max.v0_0_42_job_array_limits_max(
                                    running = slurmrestpy.models.v0_0_42_job_array_limits_max_running.v0_0_42_job_array_limits_max_running(
                                        tasks = 56, ), ), ),
                            task_id = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            task = '', ),
                        association = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_association(
                            account = '',
                            cluster = '',
                            partition = '',
                            user = '',
                            id = 56, ),
                        block = '',
                        cluster = '',
                        constraints = '',
                        container = '',
                        derived_exit_code = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code(
                            status = [
                                'INVALID'
                                ],
                            return_code = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_return_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_return_code(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            signal = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal(
                                id = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal_id.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_derived_exit_code_signal_id(
                                    set = True,
                                    infinite = True,
                                    number = 56, ),
                                name = '', ), ),
                        time = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time(
                            elapsed = 56,
                            eligible = 56,
                            end = 56,
                            planned = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_planned(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            start = 56,
                            submission = 56,
                            suspended = 56,
                            system = slurmrestpy.models.v0_0_42_job_time_system.v0_0_42_job_time_system(
                                seconds = 56,
                                microseconds = 56, ),
                            limit = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_limit.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_time_limit(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            total = slurmrestpy.models.v0_0_42_job_time_total.v0_0_42_job_time_total(
                                seconds = 56,
                                microseconds = 56, ),
                            user = slurmrestpy.models.v0_0_42_job_time_user.v0_0_42_job_time_user(
                                seconds = 56,
                                microseconds = 56, ), ),
                        exit_code = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_exit_code(),
                        extra = '',
                        failed_node = '',
                        flags = [
                            'NONE'
                            ],
                        group = '',
                        het = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het(
                            job_id = 56,
                            job_offset = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het_job_offset.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_het_job_offset(
                                set = True,
                                infinite = True,
                                number = 56, ), ),
                        job_id = 56,
                        name = '',
                        licenses = '',
                        mcs = slurmrestpy.models.v0_0_42_job_mcs.v0_0_42_job_mcs(
                            label = '', ),
                        nodes = '',
                        partition = '',
                        hold = True,
                        priority = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_priority.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_priority(
                            set = True,
                            infinite = True,
                            number = 56, ),
                        qos = '',
                        required = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required(
                            cpus = 56,
                            memory_per_cpu = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_cpu(
                                set = True,
                                infinite = True,
                                number = 56, ),
                            memory_per_node = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_node.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_required_memory_per_node(
                                set = True,
                                infinite = True,
                                number = 56, ), ),
                        kill_request_user = '',
                        reservation = slurmrestpy.models.v0_0_42_job_reservation.v0_0_42_job_reservation(
                            name = '', ),
                        script = '',
                        stdin_expanded = '',
                        stdout_expanded = '',
                        stderr_expanded = '',
                        stdout = '',
                        stderr = '',
                        stdin = '',
                        state = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_state.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_state(
                            current = [
                                'PENDING'
                                ],
                            reason = '', ),
                        steps = [
                            slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner(
                                nodes = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_nodes(
                                    count = 56,
                                    range = '',
                                    list = [
                                        ''
                                        ], ),
                                tasks = slurmrestpy.models.v0_0_42_step_tasks.v0_0_42_step_tasks(
                                    count = 56, ),
                                pid = '',
                                cpu = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU(
                                    requested_frequency = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency(
                                        min = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_cpu_requested_frequency_min.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_CPU_requested_frequency_min(
                                            set = True,
                                            infinite = True,
                                            number = 56, ), ),
                                    governor = '', ),
                                kill_request_user = '',
                                statistics = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics(
                                    energy = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy(
                                        consumed = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_statistics_energy_consumed(
                                            set = True,
                                            infinite = True,
                                            number = 56, ), ), ),
                                step = slurmrestpy.models.v0_0_42_step_step.v0_0_42_step_step(
                                    name = '', ),
                                task = slurmrestpy.models.v0_0_42_step_task.v0_0_42_step_task(
                                    distribution = '', ),
                                tres = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres(
                                    requested = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested(
                                        average = [
                                            slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                                type = '',
                                                name = '',
                                                count = 56, )
                                            ], ),
                                    allocated = [
                                        slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                                            type = '',
                                            name = '',
                                            count = 56, )
                                        ], ), )
                            ],
                        submit_line = '',
                        tres = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_tres.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_tres(),
                        used_gres = '',
                        user = '',
                        wckey = slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_wckey.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_wckey(
                            wckey = '',
                            flags = [
                                'ASSIGNED_DEFAULT'
                                ], ),
                        working_directory = '', )
                    ],
        )
        """

    def testV0041OpenapiSlurmdbdJobsResp(self):
        """Test V0041OpenapiSlurmdbdJobsResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
