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

from slurmrestpy.models.v0042_job_desc_msg import V0042JobDescMsg


class TestV0042JobDescMsg(unittest.TestCase):
    """V0042JobDescMsg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042JobDescMsg:
        """Test V0042JobDescMsg
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042JobDescMsg`
        """
        model = V0042JobDescMsg()
        if include_optional:
            return V0042JobDescMsg(
                account = '',
                account_gather_frequency = '',
                admin_comment = '',
                allocation_node_list = '',
                allocation_node_port = 56,
                argv = [
                    ''
                    ],
                array = '',
                batch_features = '',
                begin_time = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                flags = [
                    'KILL_INVALID_DEPENDENCY'
                    ],
                burst_buffer = '',
                clusters = '',
                cluster_constraint = '',
                comment = '',
                contiguous = True,
                container = '',
                container_id = '',
                core_specification = 56,
                thread_specification = 56,
                cpu_binding = '',
                cpu_binding_flags = [
                    'CPU_BIND_TO_THREADS'
                    ],
                cpu_frequency = '',
                cpus_per_tres = '',
                crontab = slurmrestpy.models.v0/0/42_cron_entry.v0.0.42_cron_entry(
                    flags = [
                        'WILD_MINUTE'
                        ],
                    minute = '',
                    hour = '',
                    day_of_month = '',
                    month = '',
                    day_of_week = '',
                    specification = '',
                    command = '',
                    line = slurmrestpy.models.v0_0_42_cron_entry_line.v0_0_42_cron_entry_line(
                        start = 56,
                        end = 56, ), ),
                deadline = 56,
                delay_boot = 56,
                dependency = '',
                end_time = 56,
                environment = [
                    ''
                    ],
                rlimits = slurmrestpy.models.v0_0_42_job_desc_msg_rlimits.v0_0_42_job_desc_msg_rlimits(
                    cpu = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    fsize = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    data = ,
                    stack = ,
                    core = ,
                    rss = ,
                    nproc = ,
                    nofile = ,
                    memlock = ,
                    as = , ),
                excluded_nodes = [
                    ''
                    ],
                extra = '',
                constraints = '',
                group_id = '',
                hetjob_group = 56,
                immediate = True,
                job_id = 56,
                kill_on_node_fail = True,
                licenses = '',
                mail_type = [
                    'BEGIN'
                    ],
                mail_user = '',
                mcs_label = '',
                memory_binding = '',
                memory_binding_type = [
                    'NONE'
                    ],
                memory_per_tres = '',
                name = '',
                network = '',
                nice = 56,
                tasks = 56,
                oom_kill_step = 56,
                open_mode = [
                    'APPEND'
                    ],
                reserve_ports = 56,
                overcommit = True,
                partition = '',
                distribution_plane_size = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                power_flags = [
                    null
                    ],
                prefer = '',
                hold = True,
                priority = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                profile = [
                    'NOT_SET'
                    ],
                qos = '',
                reboot = True,
                required_nodes = [
                    ''
                    ],
                requeue = True,
                reservation = '',
                script = '',
                shared = [
                    'none'
                    ],
                site_factor = 56,
                spank_environment = [
                    ''
                    ],
                distribution = '',
                time_limit = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                time_minimum = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                tres_bind = '',
                tres_freq = '',
                tres_per_job = '',
                tres_per_node = '',
                tres_per_socket = '',
                tres_per_task = '',
                user_id = '',
                wait_all_nodes = True,
                kill_warning_flags = [
                    'BATCH_JOB'
                    ],
                kill_warning_signal = '',
                kill_warning_delay = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                current_working_directory = '',
                cpus_per_task = 56,
                minimum_cpus = 56,
                maximum_cpus = 56,
                nodes = '',
                minimum_nodes = 56,
                maximum_nodes = 56,
                minimum_boards_per_node = 56,
                minimum_sockets_per_board = 56,
                sockets_per_node = 56,
                threads_per_core = 56,
                tasks_per_node = 56,
                tasks_per_socket = 56,
                tasks_per_core = 56,
                tasks_per_board = 56,
                ntasks_per_tres = 56,
                minimum_cpus_per_node = 56,
                memory_per_cpu = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                memory_per_node = slurmrestpy.models.v0/0/42_uint64_no_val_struct.v0.0.42_uint64_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                temporary_disk_per_node = 56,
                selinux_context = '',
                required_switches = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                segment_size = slurmrestpy.models.v0/0/42_uint16_no_val_struct.v0.0.42_uint16_no_val_struct(
                    set = True,
                    infinite = True,
                    number = 56, ),
                standard_error = '',
                standard_input = '',
                standard_output = '',
                wait_for_switch = 56,
                wckey = '',
                x11 = [
                    'FORWARD_ALL_NODES'
                    ],
                x11_magic_cookie = '',
                x11_target_host = '',
                x11_target_port = 56
            )
        else:
            return V0042JobDescMsg(
        )
        """

    def testV0042JobDescMsg(self):
        """Test V0042JobDescMsg"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
