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

from slurmrestpy.models.v0041_openapi_users_add_cond_resp_association_condition import (
    V0041OpenapiUsersAddCondRespAssociationCondition,
)


class TestV0041OpenapiUsersAddCondRespAssociationCondition(unittest.TestCase):
    """V0041OpenapiUsersAddCondRespAssociationCondition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiUsersAddCondRespAssociationCondition:
        """Test V0041OpenapiUsersAddCondRespAssociationCondition
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiUsersAddCondRespAssociationCondition`
        """
        model = V0041OpenapiUsersAddCondRespAssociationCondition()
        if include_optional:
            return V0041OpenapiUsersAddCondRespAssociationCondition(
                accounts = [
                    ''
                    ],
                association = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association.v0_0_41_openapi_users_add_cond_resp_association_condition_association(
                    comment = '',
                    defaultqos = '',
                    grpjobs = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpjobs.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpjobs(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    grpjobsaccrue = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpjobsaccrue.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpjobsaccrue(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    grpsubmitjobs = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    grptres = [
                        slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    grptresmins = [
                        slurmrestpy.models.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner.v0_0_41_openapi_slurmdbd_jobs_resp_jobs_inner_steps_inner_tres_requested_max_inner(
                            type = '',
                            name = '',
                            id = 56,
                            count = 56, )
                        ],
                    grptresrunmins = [

                        ],
                    grpwall = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpwall.v0_0_41_openapi_users_add_cond_resp_association_condition_association_grpwall(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    maxjobs = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxjobs.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxjobs(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    maxjobsaccrue = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxjobsaccrue(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    maxsubmitjobs = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxsubmitjobs.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxsubmitjobs(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    maxtresminsperjob = [

                        ],
                    maxtresrunmins = [

                        ],
                    maxtresperjob = [

                        ],
                    maxtrespernode = [

                        ],
                    maxwalldurationperjob = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob.v0_0_41_openapi_users_add_cond_resp_association_condition_association_maxwalldurationperjob(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    minpriothresh = slurmrestpy.models.v0_0_41_openapi_users_add_cond_resp_association_condition_association_minpriothresh.v0_0_41_openapi_users_add_cond_resp_association_condition_association_minpriothresh(
                        set = True,
                        infinite = True,
                        number = 56, ),
                    parent = '',
                    priority = slurmrestpy.models.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_priority.v0_0_41_openapi_slurmdbd_config_resp_associations_inner_priority(
                        set = True,
                        infinite = True,
                        number = 56, ),
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
            return V0041OpenapiUsersAddCondRespAssociationCondition(
                users = [
                    ''
                    ],
        )
        """

    def testV0041OpenapiUsersAddCondRespAssociationCondition(self):
        """Test V0041OpenapiUsersAddCondRespAssociationCondition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
