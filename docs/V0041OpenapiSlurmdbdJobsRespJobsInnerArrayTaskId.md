# V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId

Task ID of this task in job array

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional]
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional]
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional]

## Example

```python
from slurmrestpy.models.v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id import V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId

# TODO update the JSON string below
json = "{}"
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId from a JSON string
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id_instance = V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.from_json(json)
# print the JSON string representation of the object
print(V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.to_json())

# convert the object into a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id_dict = v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id_instance.to_dict()
# create an instance of V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId from a dict
v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id_from_dict = V0041OpenapiSlurmdbdJobsRespJobsInnerArrayTaskId.from_dict(v0041_openapi_slurmdbd_jobs_resp_jobs_inner_array_task_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


