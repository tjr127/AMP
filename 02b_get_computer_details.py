import requests
import env_lab  # noqa
import env_user  # noqa
import json

amp_client_id = env_user.AMP_CLIENT_ID
amp_api_key = env_user.AMP_API_KEY
print(amp_client_id)
print(amp_api_key)



# EXAMPLE:
# computer_guid = 'd7fbcdb6-0a14-4e39-867e-02f5e1649497'
computer_guid = '20f18f34-59d0-49d8-9b2e-9d81c9d99165'

url = 'https://api.amp.cisco.com/v1/computers/{}'.format(computer_guid)

request = requests.get(url, auth=(amp_client_id, amp_api_key))

json_output = request.json()
print(json_output["data"]["external_ip"])

with open('json.json', 'w') as json_file:
    json.dump(json_output, json_file)
