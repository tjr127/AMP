import requests

client_id = 'a1b2c3d4e5f6g7h8i9j0'

api_key = 'a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6'

# EXAMPLES:
# group_guid = '68665863-74d5-4bc1-ac7f-5477b2b6406e'
group_guid = '<GROUP_GUID>'

url = 'https://api.amp.cisco.com/v1/groups/{}'.format(group_guid)

response = requests.get(url, auth=(client_id, api_key))

print(response.json())