# V0042KillJobsRespJobFederation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sibling** | **str** | Name of federation sibling (may be empty for non-federation) | [optional]

## Example

```python
from slurmrestpy.models.v0042_kill_jobs_resp_job_federation import V0042KillJobsRespJobFederation

# TODO update the JSON string below
json = "{}"
# create an instance of V0042KillJobsRespJobFederation from a JSON string
v0042_kill_jobs_resp_job_federation_instance = V0042KillJobsRespJobFederation.from_json(json)
# print the JSON string representation of the object
print(V0042KillJobsRespJobFederation.to_json())

# convert the object into a dict
v0042_kill_jobs_resp_job_federation_dict = v0042_kill_jobs_resp_job_federation_instance.to_dict()
# create an instance of V0042KillJobsRespJobFederation from a dict
v0042_kill_jobs_resp_job_federation_from_dict = V0042KillJobsRespJobFederation.from_dict(v0042_kill_jobs_resp_job_federation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


