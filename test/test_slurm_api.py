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

from slurmrestpy.api.slurm_api import SlurmApi


class TestSlurmApi(unittest.TestCase):
    """SlurmApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SlurmApi()

    def tearDown(self) -> None:
        pass

    def test_slurm_v0040_delete_job(self) -> None:
        """Test case for slurm_v0040_delete_job

        cancel or signal job
        """
        pass

    def test_slurm_v0040_delete_jobs(self) -> None:
        """Test case for slurm_v0040_delete_jobs

        send signal to list of jobs
        """
        pass

    def test_slurm_v0040_delete_node(self) -> None:
        """Test case for slurm_v0040_delete_node

        delete node
        """
        pass

    def test_slurm_v0040_get_diag(self) -> None:
        """Test case for slurm_v0040_get_diag

        get diagnostics
        """
        pass

    def test_slurm_v0040_get_job(self) -> None:
        """Test case for slurm_v0040_get_job

        get job info
        """
        pass

    def test_slurm_v0040_get_jobs(self) -> None:
        """Test case for slurm_v0040_get_jobs

        get list of jobs
        """
        pass

    def test_slurm_v0040_get_jobs_state(self) -> None:
        """Test case for slurm_v0040_get_jobs_state

        get list of job states
        """
        pass

    def test_slurm_v0040_get_licenses(self) -> None:
        """Test case for slurm_v0040_get_licenses

        get all Slurm tracked license info
        """
        pass

    def test_slurm_v0040_get_node(self) -> None:
        """Test case for slurm_v0040_get_node

        get node info
        """
        pass

    def test_slurm_v0040_get_nodes(self) -> None:
        """Test case for slurm_v0040_get_nodes

        get node(s) info
        """
        pass

    def test_slurm_v0040_get_partition(self) -> None:
        """Test case for slurm_v0040_get_partition

        get partition info
        """
        pass

    def test_slurm_v0040_get_partitions(self) -> None:
        """Test case for slurm_v0040_get_partitions

        get all partition info
        """
        pass

    def test_slurm_v0040_get_ping(self) -> None:
        """Test case for slurm_v0040_get_ping

        ping test
        """
        pass

    def test_slurm_v0040_get_reconfigure(self) -> None:
        """Test case for slurm_v0040_get_reconfigure

        request slurmctld reconfigure
        """
        pass

    def test_slurm_v0040_get_reservation(self) -> None:
        """Test case for slurm_v0040_get_reservation

        get reservation info
        """
        pass

    def test_slurm_v0040_get_reservations(self) -> None:
        """Test case for slurm_v0040_get_reservations

        get all reservation info
        """
        pass

    def test_slurm_v0040_get_shares(self) -> None:
        """Test case for slurm_v0040_get_shares

        get fairshare info
        """
        pass

    def test_slurm_v0040_post_job(self) -> None:
        """Test case for slurm_v0040_post_job

        update job
        """
        pass

    def test_slurm_v0040_post_job_submit(self) -> None:
        """Test case for slurm_v0040_post_job_submit

        submit new job
        """
        pass

    def test_slurm_v0040_post_node(self) -> None:
        """Test case for slurm_v0040_post_node

        update node properties
        """
        pass

    def test_slurm_v0040_post_nodes(self) -> None:
        """Test case for slurm_v0040_post_nodes

        batch update node(s)
        """
        pass

    def test_slurm_v0041_delete_job(self) -> None:
        """Test case for slurm_v0041_delete_job

        cancel or signal job
        """
        pass

    def test_slurm_v0041_delete_jobs(self) -> None:
        """Test case for slurm_v0041_delete_jobs

        send signal to list of jobs
        """
        pass

    def test_slurm_v0041_delete_node(self) -> None:
        """Test case for slurm_v0041_delete_node

        delete node
        """
        pass

    def test_slurm_v0041_get_diag(self) -> None:
        """Test case for slurm_v0041_get_diag

        get diagnostics
        """
        pass

    def test_slurm_v0041_get_job(self) -> None:
        """Test case for slurm_v0041_get_job

        get job info
        """
        pass

    def test_slurm_v0041_get_jobs(self) -> None:
        """Test case for slurm_v0041_get_jobs

        get list of jobs
        """
        pass

    def test_slurm_v0041_get_jobs_state(self) -> None:
        """Test case for slurm_v0041_get_jobs_state

        get list of job states
        """
        pass

    def test_slurm_v0041_get_licenses(self) -> None:
        """Test case for slurm_v0041_get_licenses

        get all Slurm tracked license info
        """
        pass

    def test_slurm_v0041_get_node(self) -> None:
        """Test case for slurm_v0041_get_node

        get node info
        """
        pass

    def test_slurm_v0041_get_nodes(self) -> None:
        """Test case for slurm_v0041_get_nodes

        get node(s) info
        """
        pass

    def test_slurm_v0041_get_partition(self) -> None:
        """Test case for slurm_v0041_get_partition

        get partition info
        """
        pass

    def test_slurm_v0041_get_partitions(self) -> None:
        """Test case for slurm_v0041_get_partitions

        get all partition info
        """
        pass

    def test_slurm_v0041_get_ping(self) -> None:
        """Test case for slurm_v0041_get_ping

        ping test
        """
        pass

    def test_slurm_v0041_get_reconfigure(self) -> None:
        """Test case for slurm_v0041_get_reconfigure

        request slurmctld reconfigure
        """
        pass

    def test_slurm_v0041_get_reservation(self) -> None:
        """Test case for slurm_v0041_get_reservation

        get reservation info
        """
        pass

    def test_slurm_v0041_get_reservations(self) -> None:
        """Test case for slurm_v0041_get_reservations

        get all reservation info
        """
        pass

    def test_slurm_v0041_get_shares(self) -> None:
        """Test case for slurm_v0041_get_shares

        get fairshare info
        """
        pass

    def test_slurm_v0041_post_job(self) -> None:
        """Test case for slurm_v0041_post_job

        update job
        """
        pass

    def test_slurm_v0041_post_job_allocate(self) -> None:
        """Test case for slurm_v0041_post_job_allocate

        submit new job allocation without any steps that must be signaled to stop
        """
        pass

    def test_slurm_v0041_post_job_submit(self) -> None:
        """Test case for slurm_v0041_post_job_submit

        submit new job
        """
        pass

    def test_slurm_v0041_post_node(self) -> None:
        """Test case for slurm_v0041_post_node

        update node properties
        """
        pass

    def test_slurm_v0041_post_nodes(self) -> None:
        """Test case for slurm_v0041_post_nodes

        batch update node(s)
        """
        pass

    def test_slurm_v0042_delete_job(self) -> None:
        """Test case for slurm_v0042_delete_job

        cancel or signal job
        """
        pass

    def test_slurm_v0042_delete_jobs(self) -> None:
        """Test case for slurm_v0042_delete_jobs

        send signal to list of jobs
        """
        pass

    def test_slurm_v0042_delete_node(self) -> None:
        """Test case for slurm_v0042_delete_node

        delete node
        """
        pass

    def test_slurm_v0042_get_diag(self) -> None:
        """Test case for slurm_v0042_get_diag

        get diagnostics
        """
        pass

    def test_slurm_v0042_get_job(self) -> None:
        """Test case for slurm_v0042_get_job

        get job info
        """
        pass

    def test_slurm_v0042_get_jobs(self) -> None:
        """Test case for slurm_v0042_get_jobs

        get list of jobs
        """
        pass

    def test_slurm_v0042_get_jobs_state(self) -> None:
        """Test case for slurm_v0042_get_jobs_state

        get list of job states
        """
        pass

    def test_slurm_v0042_get_licenses(self) -> None:
        """Test case for slurm_v0042_get_licenses

        get all Slurm tracked license info
        """
        pass

    def test_slurm_v0042_get_node(self) -> None:
        """Test case for slurm_v0042_get_node

        get node info
        """
        pass

    def test_slurm_v0042_get_nodes(self) -> None:
        """Test case for slurm_v0042_get_nodes

        get node(s) info
        """
        pass

    def test_slurm_v0042_get_partition(self) -> None:
        """Test case for slurm_v0042_get_partition

        get partition info
        """
        pass

    def test_slurm_v0042_get_partitions(self) -> None:
        """Test case for slurm_v0042_get_partitions

        get all partition info
        """
        pass

    def test_slurm_v0042_get_ping(self) -> None:
        """Test case for slurm_v0042_get_ping

        ping test
        """
        pass

    def test_slurm_v0042_get_reconfigure(self) -> None:
        """Test case for slurm_v0042_get_reconfigure

        request slurmctld reconfigure
        """
        pass

    def test_slurm_v0042_get_reservation(self) -> None:
        """Test case for slurm_v0042_get_reservation

        get reservation info
        """
        pass

    def test_slurm_v0042_get_reservations(self) -> None:
        """Test case for slurm_v0042_get_reservations

        get all reservation info
        """
        pass

    def test_slurm_v0042_get_shares(self) -> None:
        """Test case for slurm_v0042_get_shares

        get fairshare info
        """
        pass

    def test_slurm_v0042_post_job(self) -> None:
        """Test case for slurm_v0042_post_job

        update job
        """
        pass

    def test_slurm_v0042_post_job_allocate(self) -> None:
        """Test case for slurm_v0042_post_job_allocate

        submit new job allocation without any steps that must be signaled to stop
        """
        pass

    def test_slurm_v0042_post_job_submit(self) -> None:
        """Test case for slurm_v0042_post_job_submit

        submit new job
        """
        pass

    def test_slurm_v0042_post_node(self) -> None:
        """Test case for slurm_v0042_post_node

        update node properties
        """
        pass

    def test_slurm_v0042_post_nodes(self) -> None:
        """Test case for slurm_v0042_post_nodes

        batch update node(s)
        """
        pass


if __name__ == "__main__":
    unittest.main()
