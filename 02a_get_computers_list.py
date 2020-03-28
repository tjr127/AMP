import requests
import json
from pathlib import Path
import sys
from pprint import pprint

import env_lab  # noqa
import env_user  # noqa

here = Path(__file__).parent.absolute()
repository_root = (here / ".." ).resolve()

sys.path.insert(0, str(repository_root))

amp_client_id = env_user.AMP_CLIENT_ID
amp_api_key = env_user.AMP_API_KEY
print(amp_client_id)
print(amp_api_key)

url = 'https://api.amp.cisco.com/v1/computers'

request = requests.get(url, auth=(amp_client_id, amp_api_key))

#print(request.content)
#print(type(request.content))
#print (type((request.json())))
#print(json.loads(request))
json_output = request.json()
json_formatted = json.dumps(json_output, sort_keys=True, indent=4)
#print(json_output)
#print(type(json_output))
#pprint(request.json())
print(json_output['data'][0]['internal_ips'][0])

with open('json.json', 'w') as json_file:
    json.dump(json_output, json_file)