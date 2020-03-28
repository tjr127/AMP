import requests

#here = Path(__file__).parent.absolute()
#repository_root = (here / ".." ).resolve()

#sys.path.insert(0, str(repository_root))

import env_lab  # noqa
import env_user  # noqa

amp_client_id = env_user.AMP_CLIENT_ID
amp_api_key = env_user.AMP_API_KEY
print(amp_client_id)
print(amp_api_key)

url = 'https://api.amp.cisco.com/v1/version'

request = requests.get(url, auth=(amp_client_id, amp_api_key))

print(request.json())
