import requests
import json

amp_client_id = 'a1b2c3d4e5f6g7h8i9j0'

amp_api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLE:
# stream_id = '7213'
stream_id = '<STREAM_ID>'

url = 'https://api.amp.cisco.com/v1/event_streams/{}'.format(stream_id)

request = requests.delete(url, auth=(amp_client_id, amp_api_key))

print(request.json())
