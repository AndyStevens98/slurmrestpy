# V0040KillJobsRespJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**V0042KillJobsRespJobError**](V0042KillJobsRespJobError.md) |  | [optional]
**step_id** | **str** | Job or Step ID that signaling failed |
**job_id** | [**V0040Uint32NoVal**](V0040Uint32NoVal.md) |  |
**federation** | [**V0042KillJobsRespJobFederation**](V0042KillJobsRespJobFederation.md) |  | [optional]

## Example

```python
from slurmrestpy.models.v0040_kill_jobs_resp_job import V0040KillJobsRespJob

# TODO update the JSON string below
json = "{}"
# create an instance of V0040KillJobsRespJob from a JSON string
v0040_kill_jobs_resp_job_instance = V0040KillJobsRespJob.from_json(json)
# print the JSON string representation of the object
print(V0040KillJobsRespJob.to_json())

# convert the object into a dict
v0040_kill_jobs_resp_job_dict = v0040_kill_jobs_resp_job_instance.to_dict()
# create an instance of V0040KillJobsRespJob from a dict
v0040_kill_jobs_resp_job_from_dict = V0040KillJobsRespJob.from_dict(v0040_kill_jobs_resp_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


