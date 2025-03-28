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

from slurmrestpy.models.v0041_openapi_users_add_cond_resp_association_condition_association_grpsubmitjobs import (
    V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs,
)


class TestV0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs(
    unittest.TestCase
):
    """V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs:
        """Test V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs`
        """
        model = V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs()
        if include_optional:
            return V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs(
                set = True,
                infinite = True,
                number = 56
            )
        else:
            return V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs(
        )
        """

    def testV0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs(
        self,
    ):
        """Test V0041OpenapiUsersAddCondRespAssociationConditionAssociationGrpsubmitjobs"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
