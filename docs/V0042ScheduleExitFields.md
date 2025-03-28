# V0042ScheduleExitFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_job_queue** | **int** | Reached end of queue | [optional]
**default_queue_depth** | **int** | Reached number of jobs allowed to be tested | [optional]
**max_job_start** | **int** | Reached number of jobs allowed to start | [optional]
**max_rpc_cnt** | **int** | Reached RPC limit | [optional]
**max_sched_time** | **int** | Reached maximum allowed scheduler time | [optional]
**licenses** | **int** | Blocked on licenses | [optional]

## Example

```python
from slurmrestpy.models.v0042_schedule_exit_fields import V0042ScheduleExitFields

# TODO update the JSON string below
json = "{}"
# create an instance of V0042ScheduleExitFields from a JSON string
v0042_schedule_exit_fields_instance = V0042ScheduleExitFields.from_json(json)
# print the JSON string representation of the object
print(V0042ScheduleExitFields.to_json())

# convert the object into a dict
v0042_schedule_exit_fields_dict = v0042_schedule_exit_fields_instance.to_dict()
# create an instance of V0042ScheduleExitFields from a dict
v0042_schedule_exit_fields_from_dict = V0042ScheduleExitFields.from_dict(v0042_schedule_exit_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


