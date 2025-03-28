# V0041UpdateNodeMsgWeight

Weight of the node for scheduling purposes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | True if number has been set; False if number is unset | [optional]
**infinite** | **bool** | True if number has been set to infinite; \&quot;set\&quot; and \&quot;number\&quot; will be ignored | [optional]
**number** | **int** | If \&quot;set\&quot; is True the number will be set with value; otherwise ignore number contents | [optional]

## Example

```python
from slurmrestpy.models.v0041_update_node_msg_weight import V0041UpdateNodeMsgWeight

# TODO update the JSON string below
json = "{}"
# create an instance of V0041UpdateNodeMsgWeight from a JSON string
v0041_update_node_msg_weight_instance = V0041UpdateNodeMsgWeight.from_json(json)
# print the JSON string representation of the object
print(V0041UpdateNodeMsgWeight.to_json())

# convert the object into a dict
v0041_update_node_msg_weight_dict = v0041_update_node_msg_weight_instance.to_dict()
# create an instance of V0041UpdateNodeMsgWeight from a dict
v0041_update_node_msg_weight_from_dict = V0041UpdateNodeMsgWeight.from_dict(v0041_update_node_msg_weight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


