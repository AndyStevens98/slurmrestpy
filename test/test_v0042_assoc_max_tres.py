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

from slurmrestpy.models.v0042_assoc_max_tres import V0042AssocMaxTres


class TestV0042AssocMaxTres(unittest.TestCase):
    """V0042AssocMaxTres unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042AssocMaxTres:
        """Test V0042AssocMaxTres
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042AssocMaxTres`
        """
        model = V0042AssocMaxTres()
        if include_optional:
            return V0042AssocMaxTres(
                total = [
                    slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                        type = '',
                        name = '',
                        id = 56,
                        count = 56, )
                    ],
                group = slurmrestpy.models.v0_0_42_assoc_max_tres_group.v0_0_42_assoc_max_tres_group(
                    minutes = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    active = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ], ),
                minutes = slurmrestpy.models.v0_0_42_assoc_max_tres_minutes.v0_0_42_assoc_max_tres_minutes(
                    total = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    per = slurmrestpy.models.v0_0_42_qos_limits_min_tres_per.v0_0_42_qos_limits_min_tres_per(
                        job = [
                            slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                                type = '',
                                name = '',
                                id = 56,
                                count = 56, )
                            ], ), ),
                per = slurmrestpy.models.v0_0_42_assoc_max_tres_per.v0_0_42_assoc_max_tres_per(
                    job = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    node = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ], )
            )
        else:
            return V0042AssocMaxTres(
        )
        """

    def testV0042AssocMaxTres(self):
        """Test V0042AssocMaxTres"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
