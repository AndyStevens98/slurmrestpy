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

from slurmrestpy.models.v0042_users_add_cond import V0042UsersAddCond


class TestV0042UsersAddCond(unittest.TestCase):
    """V0042UsersAddCond unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V0042UsersAddCond:
        """Test V0042UsersAddCond
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0042UsersAddCond`
        """
        model = V0042UsersAddCond()
        if include_optional:
            return V0042UsersAddCond(
                accounts = [
                    ''
                    ],
                association = slurmrestpy.models.v0/0/42_assoc_rec_set.v0.0.42_assoc_rec_set(
                    comment = '',
                    defaultqos = '',
                    grpjobs = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    grpjobsaccrue = slurmrestpy.models.v0/0/42_uint32_no_val_struct.v0.0.42_uint32_no_val_struct(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    grpsubmitjobs = ,
                    grptres = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    grptresmins = [
                        slurmrestpy.models.v0/0/42_tres.v0.0.42_tres(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    grptresrunmins = ,
                    grpwall = ,
                    maxjobs = ,
                    maxjobsaccrue = ,
                    maxsubmitjobs = ,
                    maxtresminsperjob = ,
                    maxtresrunmins = ,
                    maxtresperjob = ,
                    maxtrespernode = ,
                    maxwalldurationperjob = ,
                    minpriothresh = ,
                    parent = '',
                    priority = ,
                    qoslevel = [
                        ''
                        ],
                    fairshare = 56, ),
                clusters = [
                    ''
                    ],
                partitions = [
                    ''
                    ],
                users = [
                    ''
                    ],
                wckeys = [
                    ''
                    ]
            )
        else:
            return V0042UsersAddCond(
                users = [
                    ''
                    ],
        )
        """

    def testV0042UsersAddCond(self):
        """Test V0042UsersAddCond"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
