# V0042QosPreempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**list** | **List[str]** |  | [optional]
**mode** | **List[str]** |  | [optional]
**exempt_time** | [**V0042Uint32NoValStruct**](V0042Uint32NoValStruct.md) |  | [optional]

## Example

```python
from slurmrestpy.models.v0042_qos_preempt import V0042QosPreempt

# TODO update the JSON string below
json = "{}"
# create an instance of V0042QosPreempt from a JSON string
v0042_qos_preempt_instance = V0042QosPreempt.from_json(json)
# print the JSON string representation of the object
print(V0042QosPreempt.to_json())

# convert the object into a dict
v0042_qos_preempt_dict = v0042_qos_preempt_instance.to_dict()
# create an instance of V0042QosPreempt from a dict
v0042_qos_preempt_from_dict = V0042QosPreempt.from_dict(v0042_qos_preempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


