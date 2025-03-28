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

from slurmrestpy.models.v0042_openapi_diag_resp import V0042OpenapiDiagResp


class TestV0042OpenapiDiagResp(unittest.TestCase):
    """V0042OpenapiDiagResp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042OpenapiDiagResp:
        """Test V0042OpenapiDiagResp
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042OpenapiDiagResp`
        """
        model = V0042OpenapiDiagResp()
        if include_optional:
            return V0042OpenapiDiagResp(
                statistics = slurmrestpy.models.v0/0/42_stats_msg.v0.0.42_stats_msg(
                    parts_packed = 56,
                    req_time = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    req_time_start = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    server_thread_count = 56,
                    agent_queue_size = 56,
                    agent_count = 56,
                    agent_thread_count = 56,
                    dbd_agent_queue_size = 56,
                    gettimeofday_latency = 56,
                    schedule_cycle_max = 56,
                    schedule_cycle_last = 56,
                    schedule_cycle_sum = 56,
                    schedule_cycle_total = 56,
                    schedule_cycle_mean = 56,
                    schedule_cycle_mean_depth = 56,
                    schedule_cycle_per_minute = 56,
                    schedule_cycle_depth = 56,
                    schedule_exit = slurmrestpy.models.v0/0/42_schedule_exit_fields.v0.0.42_schedule_exit_fields(
                        end_job_queue = 56,
                        default_queue_depth = 56,
                        max_job_start = 56,
                        max_rpc_cnt = 56,
                        max_sched_time = 56,
                        licenses = 56, ),
                    schedule_queue_length = 56,
                    jobs_submitted = 56,
                    jobs_started = 56,
                    jobs_completed = 56,
                    jobs_canceled = 56,
                    jobs_failed = 56,
                    jobs_pending = 56,
                    jobs_running = 56,
                    job_states_ts = ,
                    bf_backfilled_jobs = 56,
                    bf_last_backfilled_jobs = 56,
                    bf_backfilled_het_jobs = 56,
                    bf_cycle_counter = 56,
                    bf_cycle_mean = 56,
                    bf_depth_mean = 56,
                    bf_depth_mean_try = 56,
                    bf_cycle_sum = 56,
                    bf_cycle_last = 56,
                    bf_cycle_max = 56,
                    bf_exit = slurmrestpy.models.v0/0/42_bf_exit_fields.v0.0.42_bf_exit_fields(
                        end_job_queue = 56,
                        bf_max_job_start = 56,
                        bf_max_job_test = 56,
                        bf_max_time = 56,
                        bf_node_space_size = 56,
                        state_changed = 56, ),
                    bf_last_depth = 56,
                    bf_last_depth_try = 56,
                    bf_depth_sum = 56,
                    bf_depth_try_sum = 56,
                    bf_queue_len = 56,
                    bf_queue_len_mean = 56,
                    bf_queue_len_sum = 56,
                    bf_table_size = 56,
                    bf_table_size_sum = 56,
                    bf_table_size_mean = 56,
                    bf_when_last_cycle = ,
                    bf_active = True,
                    rpcs_by_message_type = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_type.v0.0.42_stats_msg_rpc_type(
                            type_id = 56,
                            message_type = '',
                            count = 56,
                            queued = 56,
                            dropped = 56,
                            cycle_last = 56,
                            cycle_max = 56,
                            total_time = 56,
                            average_time = , )
                        ],
                    rpcs_by_user = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_user.v0.0.42_stats_msg_rpc_user(
                            user_id = 56,
                            user = '',
                            count = 56,
                            total_time = 56,
                            average_time = , )
                        ],
                    pending_rpcs = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_queue.v0.0.42_stats_msg_rpc_queue(
                            type_id = 56,
                            message_type = '',
                            count = 56, )
                        ],
                    pending_rpcs_by_hostlist = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_dump.v0.0.42_stats_msg_rpc_dump(
                            type_id = 56,
                            message_type = '',
                            count = [
                                ''
                                ], )
                        ], ),
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
            return V0042OpenapiDiagResp(
                statistics = slurmrestpy.models.v0/0/42_stats_msg.v0.0.42_stats_msg(
                    parts_packed = 56,
                    req_time = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    req_time_start = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    server_thread_count = 56,
                    agent_queue_size = 56,
                    agent_count = 56,
                    agent_thread_count = 56,
                    dbd_agent_queue_size = 56,
                    gettimeofday_latency = 56,
                    schedule_cycle_max = 56,
                    schedule_cycle_last = 56,
                    schedule_cycle_sum = 56,
                    schedule_cycle_total = 56,
                    schedule_cycle_mean = 56,
                    schedule_cycle_mean_depth = 56,
                    schedule_cycle_per_minute = 56,
                    schedule_cycle_depth = 56,
                    schedule_exit = slurmrestpy.models.v0/0/42_schedule_exit_fields.v0.0.42_schedule_exit_fields(
                        end_job_queue = 56,
                        default_queue_depth = 56,
                        max_job_start = 56,
                        max_rpc_cnt = 56,
                        max_sched_time = 56,
                        licenses = 56, ),
                    schedule_queue_length = 56,
                    jobs_submitted = 56,
                    jobs_started = 56,
                    jobs_completed = 56,
                    jobs_canceled = 56,
                    jobs_failed = 56,
                    jobs_pending = 56,
                    jobs_running = 56,
                    job_states_ts = ,
                    bf_backfilled_jobs = 56,
                    bf_last_backfilled_jobs = 56,
                    bf_backfilled_het_jobs = 56,
                    bf_cycle_counter = 56,
                    bf_cycle_mean = 56,
                    bf_depth_mean = 56,
                    bf_depth_mean_try = 56,
                    bf_cycle_sum = 56,
                    bf_cycle_last = 56,
                    bf_cycle_max = 56,
                    bf_exit = slurmrestpy.models.v0/0/42_bf_exit_fields.v0.0.42_bf_exit_fields(
                        end_job_queue = 56,
                        bf_max_job_start = 56,
                        bf_max_job_test = 56,
                        bf_max_time = 56,
                        bf_node_space_size = 56,
                        state_changed = 56, ),
                    bf_last_depth = 56,
                    bf_last_depth_try = 56,
                    bf_depth_sum = 56,
                    bf_depth_try_sum = 56,
                    bf_queue_len = 56,
                    bf_queue_len_mean = 56,
                    bf_queue_len_sum = 56,
                    bf_table_size = 56,
                    bf_table_size_sum = 56,
                    bf_table_size_mean = 56,
                    bf_when_last_cycle = ,
                    bf_active = True,
                    rpcs_by_message_type = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_type.v0.0.42_stats_msg_rpc_type(
                            type_id = 56,
                            message_type = '',
                            count = 56,
                            queued = 56,
                            dropped = 56,
                            cycle_last = 56,
                            cycle_max = 56,
                            total_time = 56,
                            average_time = , )
                        ],
                    rpcs_by_user = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_user.v0.0.42_stats_msg_rpc_user(
                            user_id = 56,
                            user = '',
                            count = 56,
                            total_time = 56,
                            average_time = , )
                        ],
                    pending_rpcs = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_queue.v0.0.42_stats_msg_rpc_queue(
                            type_id = 56,
                            message_type = '',
                            count = 56, )
                        ],
                    pending_rpcs_by_hostlist = [
                        slurmrestpy.models.v0/0/42_stats_msg_rpc_dump.v0.0.42_stats_msg_rpc_dump(
                            type_id = 56,
                            message_type = '',
                            count = [
                                ''
                                ], )
                        ], ),
        )
        """

    def testV0042OpenapiDiagResp(self):
        """Test V0042OpenapiDiagResp"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
