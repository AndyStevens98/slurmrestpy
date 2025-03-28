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

from slurmrestpy.models.v0042_rollup_stats_daily_duration import (
    V0042RollupStatsDailyDuration,
)


class TestV0042RollupStatsDailyDuration(unittest.TestCase):
    """V0042RollupStatsDailyDuration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042RollupStatsDailyDuration:
        """Test V0042RollupStatsDailyDuration
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042RollupStatsDailyDuration`
        """
        model = V0042RollupStatsDailyDuration()
        if include_optional:
            return V0042RollupStatsDailyDuration(
                last = 56,
                max = 56,
                time = 56
            )
        else:
            return V0042RollupStatsDailyDuration(
        )
        """

    def testV0042RollupStatsDailyDuration(self):
        """Test V0042RollupStatsDailyDuration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
